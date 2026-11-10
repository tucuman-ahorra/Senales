#!/usr/bin/env python3
"""
Escáner multipar. Cada vez que corre:
  1) baja velas de 5 min de cada par (Twelve Data con clave; si falla, Yahoo Finance),
  2) las agrupa en velas de 15 min (u otras, ver pares.json) y deja solo las ya cerradas,
  3) calcula los indicadores y el nivel de señal de CADA vela,
  4) registra, para cada vela nueva, cuál habría sido el resultado de entrar en la vela siguiente.
  5) (opcional) evalúa el MODELO de 30 min de cada par; si marca señal en la vela que acaba de cerrar, manda un aviso
     al celular con ntfy (ver README) y guarda la señal con su resultado en datos/modelo_AAAA-MM.csv.
Guarda todo en datos/AAAA-MM.csv. No necesita que nadie anote nada: el resultado es teórico y automático.
Las velas ya registradas no se repiten, y si se saltea una corrida, la siguiente recupera lo que faltó.
"""
import os, sys, json, time
from pathlib import Path
import numpy as np, pandas as pd, requests
import modelo

RAIZ = Path(__file__).resolve().parent
DATOS = RAIZ / "datos"
UM = 2.5
COLUMNAS = ["par", "min", "t_senal", "hora_utc", "dsem", "z20", "z80", "rsi14", "estoc14", "vol",
            "dir", "nivel", "entrada", "salida", "sube", "empate"]

# ---------------------------------------------------------------- indicadores
def rsi(c, n=14):
    d = c.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / (dn + 1e-12))

def indicadores(v):
    o, h, l, c = v.o, v.h, v.l, v.c
    out = pd.DataFrame(index=v.index)
    out["z20"] = (c - c.rolling(20).mean()) / c.rolling(20).std()
    out["z80"] = (c - c.rolling(80).mean()) / c.rolling(80).std()
    out["rsi14"] = rsi(c, 14)
    ll, hh = l.rolling(14).min(), h.rolling(14).max()
    out["estoc14"] = 100 * (c - ll) / (hh - ll + 1e-12)
    atr = (h - l).rolling(14).mean()
    out["vol"] = atr / atr.rolling(100).mean()
    return out

def clasificar(z20, z80, rsi14, est):
    """Devuelve (dir, nivel). dir: 1 = comprar (sube), -1 = vender (baja), 0 = sin señal.
    nivel: 0 ninguno, 1 normal, 2 fuerte, 3 muy fuerte (mismas reglas que la herramienta web)."""
    if z20 <= -UM: d = 1
    elif z20 >= UM: d = -1
    else: return 0, 0
    nivel = 1
    ok = (rsi14 < 30 and est < 20) if d == 1 else (rsi14 > 70 and est > 80)
    if ok:
        nivel = 2
        if (z80 <= -1.5) if d == 1 else (z80 >= 1.5): nivel = 3
    return d, nivel

# ---------------------------------------------------------------- datos de entrada
def agrupar(b5, k, ahora):
    g = b5.resample(f"{k}min", label="left", closed="left").agg(
        o=("o", "first"), h=("h", "max"), l=("l", "min"), c=("c", "last"), n=("c", "count"))
    g = g[g.n == k // 5]                                   # solo velas completas
    g = g[g.index + pd.Timedelta(minutes=k) <= ahora]      # solo velas ya cerradas
    return g.drop(columns="n")

def bajar_td(simbolo, clave):
    r = requests.get("https://api.twelvedata.com/time_series", timeout=40, params=dict(
        symbol=simbolo, interval="5min", outputsize=1500, timezone="UTC", order="ASC", apikey=clave))
    j = r.json()
    if j.get("status") == "error" or "values" not in j:
        raise RuntimeError("Twelve Data: " + str(j.get("message", "respuesta inválida")))
    d = pd.DataFrame(j["values"])
    d["t"] = pd.to_datetime(d["datetime"], utc=True)
    for c in ("open", "high", "low", "close"): d[c] = d[c].astype(float)
    return d.rename(columns={"open": "o", "high": "h", "low": "l", "close": "c"}).set_index("t")[["o", "h", "l", "c"]].sort_index()

def bajar_yahoo(simbolo):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{simbolo}?interval=5m&range=7d"
    r = requests.get(u, timeout=40, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    res = r.json()["chart"]["result"][0]; q = res["indicators"]["quote"][0]
    d = pd.DataFrame({"o": q["open"], "h": q["high"], "l": q["low"], "c": q["close"]},
                     index=pd.to_datetime(res["timestamp"], unit="s", utc=True)).dropna()
    return d

def bajar(par, clave):
    if clave:
        try: return bajar_td(par["nombre"], clave)
        except Exception as e: print(f"  aviso {par['nombre']}: {e}; pruebo con Yahoo", flush=True)
    return bajar_yahoo(par["yahoo"])

# ---------------------------------------------------------------- registro
def cargar_estado():
    f = DATOS / "estado.json"
    return json.loads(f.read_text()) if f.exists() else {}

def guardar_estado(e):
    DATOS.mkdir(exist_ok=True)
    (DATOS / "estado.json").write_text(json.dumps(e, indent=1, sort_keys=True))

def procesar(nombre, b5, k, ahora, estado, escribir=True):
    """Agrega al registro las velas nuevas. Devuelve la lista de filas nuevas."""
    g = agrupar(b5, k, ahora)
    if len(g) < 120:
        print(f"  {nombre} {k}min: pocas velas ({len(g)})", flush=True); return []
    ind = indicadores(g); t = g.index
    clave = f"{nombre}|{k}"
    ultimo = pd.Timestamp(estado[clave]) if clave in estado else None
    filas = []
    for i in range(len(g) - 1):
        ent = t[i + 1]
        if ultimo is not None and ent <= ultimo: continue
        if ent - t[i] != pd.Timedelta(minutes=k): continue         # sin huecos
        r = ind.iloc[i]
        if r.isna().any(): continue
        d, nivel = clasificar(r.z20, r.z80, r.rsi14, r.estoc14)
        o1, c1 = g.o.iloc[i + 1], g.c.iloc[i + 1]
        filas.append([nombre, k, (t[i] + pd.Timedelta(minutes=k)).strftime("%Y-%m-%d %H:%M"), ent.hour, ent.dayofweek,
                      round(r.z20, 3), round(r.z80, 3), round(r.rsi14, 2), round(r.estoc14, 2), round(r.vol, 3),
                      d, nivel, o1, c1, int(c1 > o1), int(c1 == o1)])
    if len(g) >= 2: estado[clave] = t[-1].isoformat()
    if escribir and filas: escribir_filas(filas)
    return filas

def escribir_filas(filas):
    DATOS.mkdir(exist_ok=True)
    df = pd.DataFrame(filas, columns=COLUMNAS)
    df["mes"] = df["t_senal"].str[:7]
    for mes, parte in df.groupby("mes"):
        f = DATOS / f"{mes}.csv"
        parte = parte.drop(columns="mes")
        if f.exists():
            ya = pd.read_csv(f, usecols=["par", "min", "t_senal"])
            claves = set(zip(ya.par, ya["min"], ya.t_senal))
            parte = parte[[(a, b, c) not in claves for a, b, c in zip(parte.par, parte["min"], parte.t_senal)]]
        if len(parte):
            parte.to_csv(f, mode="a", header=not f.exists(), index=False)

# ---------------------------------------------------------------- modelo de 30 min + avisos
COLUMNAS_MOD = ["par", "t_senal", "hora_utc", "p", "dir", "conf", "entrada", "salida", "sube", "empate"]
LIMITE_AVISO_MIN = 12   # si la vela cerró hace más de esto, el aviso llegaría tarde: no se manda

def mercado_cerrado(ahora):
    wd, h = ahora.dayofweek, ahora.hour
    return wd == 5 or (wd == 4 and h >= 22) or (wd == 6 and h < 21)

def hora_local(ts):
    try:
        from zoneinfo import ZoneInfo
        return ts.tz_convert(ZoneInfo("America/Argentina/Tucuman")).strftime("%H:%M")
    except Exception:
        return (ts - pd.Timedelta(hours=3)).strftime("%H:%M")

def notificar(tema, titulo, mensaje, prioridad=4):
    """Aviso push a través de ntfy.sh (gratis; la app ntfy escucha tu tema secreto)."""
    r = requests.post("https://ntfy.sh/", timeout=20, json=dict(
        topic=tema, title=titulo, message=mensaje, priority=prioridad, tags=["chart_with_upwards_trend"]))
    r.raise_for_status()

def procesar_modelo(nombre, b5, ahora, estado, tema="", escribir=True, avisar=None):
    """Registra las señales del modelo (con su resultado) y avisa de la que acaba de cerrar. Devuelve (filas, avisos)."""
    g = agrupar(b5, 30, ahora)
    if len(g) < modelo.MIN_VELAS:
        print(f"  {nombre} modelo: pocas velas ({len(g)})", flush=True); return [], 0
    ev = modelo.evaluar(g, nombre); t = g.index
    clave = f"modelo|{nombre}"
    ultimo = pd.Timestamp(estado[clave]) if clave in estado else None
    filas = []
    for i in range(len(g) - 1):
        ent = t[i + 1]
        if ultimo is not None and ent <= ultimo: continue
        if ent - t[i] != pd.Timedelta(minutes=30): continue
        r = ev.iloc[i]
        if not r.sen: continue
        o1, c1 = g.o.iloc[i + 1], g.c.iloc[i + 1]
        filas.append([nombre, (t[i] + pd.Timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M"), ent.hour, round(r.p, 4),
                      int(r.dir), round(r.conf, 4), o1, c1, int(c1 > o1), int(c1 == o1)])
    estado[clave] = t[-1].isoformat()
    if escribir and filas: escribir_modelo(filas)
    # aviso de la vela que acaba de cerrar
    avisos = 0; r = ev.iloc[-1]; cierre = t[-1] + pd.Timedelta(minutes=30)
    if r.sen and tema:
        edad = (ahora - cierre).total_seconds() / 60; marca = cierre.strftime("%Y-%m-%d %H:%M")
        if edad <= LIMITE_AVISO_MIN and estado.get(f"aviso|{nombre}") != marca:
            pu = r.p if r.dir == 1 else 1 - r.p
            try:
                (avisar or notificar)(tema, f"{'COMPRAR ▲' if r.dir == 1 else 'VENDER ▼'} {nombre} · 30 min",
                       f"Modelo: probabilidad {pu*100:.0f}%. La vela cerró a las {hora_local(cierre)}; entrá ahora y vence a las {hora_local(cierre + pd.Timedelta(minutes=30))} (hora de Tucumán).")
                estado[f"aviso|{nombre}"] = marca; avisos = 1
            except Exception as e:
                print(f"  aviso {nombre}: no se pudo enviar ({e})", flush=True)
        elif edad > LIMITE_AVISO_MIN:
            print(f"  {nombre}: señal del modelo, pero cerró hace {edad:.0f} min (muy tarde para avisar)", flush=True)
    return filas, avisos

def escribir_modelo(filas):
    DATOS.mkdir(exist_ok=True)
    df = pd.DataFrame(filas, columns=COLUMNAS_MOD)
    df["mes"] = df["t_senal"].str[:7]
    for mes, parte in df.groupby("mes"):
        f = DATOS / f"modelo_{mes}.csv"; parte = parte.drop(columns="mes")
        if f.exists():
            ya = pd.read_csv(f, usecols=["par", "t_senal"]); claves = set(zip(ya.par, ya.t_senal))
            parte = parte[[(a, b) not in claves for a, b in zip(parte.par, parte.t_senal)]]
        if len(parte): parte.to_csv(f, mode="a", header=not f.exists(), index=False)

def ahora_utc():
    return pd.Timestamp.now(tz="UTC")

def dormir(seg):
    time.sleep(max(0, seg))

def una_pasada(cfg, clave, tema):
    """Una vuelta completa por todos los pares. Devuelve False si el mercado está cerrado."""
    ahora = ahora_utc(); estado = cargar_estado(); total = 0
    if mercado_cerrado(ahora) and not os.environ.get("FORZAR"):
        print(f"[{ahora:%H:%M}] Mercado cerrado: no se consulta nada.", flush=True); return False
    print(f"[{ahora:%Y-%m-%d %H:%M:%S} UTC] Pasada nueva", flush=True)
    for p in cfg["pares"]:
        try:
            b5 = bajar(p, clave)
            for k in cfg["intervalos"]:
                n = len(procesar(p["nombre"], b5, k, ahora, estado)); total += n
                print(f"  {p['nombre']} {k}min: {n} velas nuevas", flush=True)
            if cfg.get("modelo_30min", True):
                f, a = procesar_modelo(p["nombre"], b5, ahora, estado, tema)
                print(f"  {p['nombre']} modelo 30min: {len(f)} señales registradas, {a} aviso(s)", flush=True)
        except Exception as e:
            print(f"  ERROR {p['nombre']}: {e}", flush=True)
        guardar_estado(estado)
        dormir(cfg.get("pausa_seg", 8))
    print("Pasada lista. Filas nuevas:", total, flush=True)
    return True

def guardar_git():
    """Sube a GitHub lo nuevo de datos/ (así el informe y los registros se ven apenas se generan)."""
    import subprocess
    try:
        subprocess.run([sys.executable, "analizar.py"], cwd=RAIZ, stdout=subprocess.DEVNULL, timeout=180)
        run = lambda *a: subprocess.run(["git", *a], cwd=RAIZ, capture_output=True, text=True, timeout=120)
        run("add", "datos")
        if run("diff", "--staged", "--quiet").returncode == 0: return
        run("commit", "-m", f"datos {ahora_utc():%Y-%m-%d %H:%M}")
        run("pull", "--rebase"); r = run("push")
        if r.returncode: print("  aviso: no se pudo subir:", r.stderr.strip()[:200], flush=True)
    except Exception as e:
        print("  aviso: no se pudo subir:", e, flush=True)

def proximo_cierre(ahora):
    """Próximo cierre de vela de 30 min (hh:00 o hh:30 UTC) más 25 segundos de margen para que el proveedor publique la última vela de 5 min."""
    return ahora.floor("30min") + pd.Timedelta(minutes=30, seconds=25)

def main():
    cfg = json.loads((RAIZ / "pares.json").read_text())
    clave = os.environ.get("TD_KEY", "").strip()
    print("Fuente:", "Twelve Data (con Yahoo de respaldo)" if clave else "Yahoo Finance (sin clave)", flush=True)
    tema = os.environ.get("NTFY_TOPIC", "").strip() if cfg.get("modelo_30min", True) else ""
    if cfg.get("modelo_30min", True) and not tema:
        print("Aviso: no hay NTFY_TOPIC; el modelo se registra pero no se mandan avisos al celular.", flush=True)
    if "--bucle" not in sys.argv:
        una_pasada(cfg, clave, tema); return
    # Modo bucle: queda trabajando casi 6 horas y corre justo después de cada cierre de vela de 30 min.
    # GitHub reinicia la tarea solo cada hora (ver escaner.yml); mientras tanto no depende de los atrasos del reloj programado.
    inicio = ahora_utc(); fin = inicio + pd.Timedelta(minutes=cfg.get("bucle_minutos", 340))
    una_pasada(cfg, clave, tema); guardar_git()
    while True:
        objetivo = proximo_cierre(ahora_utc())
        if objetivo > fin: break
        dormir((objetivo - ahora_utc()).total_seconds())
        una_pasada(cfg, clave, tema); guardar_git()
    print("Fin del turno; GitHub arranca el siguiente.", flush=True)

if __name__ == "__main__":
    main()
