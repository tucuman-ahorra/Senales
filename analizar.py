#!/usr/bin/env python3
"""
Lee datos/*.csv (lo que registra escaner.py) y escribe datos/informe.md con:
  - resultados por par y por nivel de señal (acierto, rango razonable, ganancia esperada),
  - corrección por comparaciones múltiples (Holm): con muchos pares, alguno parece bueno por azar,
    y esta corrección dice cuáles superan el equilibrio de forma que el azar no explica.
Uso:  python analizar.py            (genera datos/informe.md y lo imprime)
"""
import glob, json, math
from pathlib import Path
import numpy as np, pandas as pd

RAIZ = Path(__file__).resolve().parent
DATOS = RAIZ / "datos"
cfg = json.loads((RAIZ / "pares.json").read_text())
PAGO = cfg.get("pago", 0.90)
EQ = 1 / (1 + PAGO)
GRUPOS = [("Normal o mejor (nivel ≥ 1)", 1), ("Fuerte o mejor (nivel ≥ 2)", 2), ("Muy fuerte (nivel 3)", 3)]
MIN_N = 30

def wilson(w, n, z=1.96):
    p = w / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h

def p_valor(w, n):
    """Probabilidad (una cola) de acertar tanto o más por puro azar si la verdadera chance fuera el equilibrio."""
    z = (w / n - EQ) / math.sqrt(EQ * (1 - EQ) / n)
    return 0.5 * math.erfc(z / math.sqrt(2))

def holm(pvals, alfa=0.05):
    orden = sorted(range(len(pvals)), key=lambda i: pvals[i]); m = len(pvals); ok = [False] * m
    for r, i in enumerate(orden):
        if pvals[i] <= alfa / (m - r): ok[i] = True
        else: break
    return ok

def cargar():
    fs = sorted(glob.glob(str(DATOS / "20*.csv")))
    if not fs: return None
    d = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
    d = d.drop_duplicates(["par", "min", "t_senal"])
    d["gana"] = (((d["dir"] == 1) & (d.sube == 1)) | ((d["dir"] == -1) & (d.sube == 0))) & (d.empate == 0)
    return d

def seccion_modelo():
    """Resultados en vivo del modelo de 30 minutos (datos/modelo_AAAA-MM.csv): la prueba que falta."""
    fs = sorted(glob.glob(str(DATOS / "modelo_*.csv")))
    if not fs: return ["## Modelo de 30 minutos (en vivo)", "", "Todavía no hay señales registradas.", ""]
    m = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True).drop_duplicates(["par", "t_senal"])
    m["gana"] = (((m["dir"] == 1) & (m.sube == 1)) | ((m["dir"] == -1) & (m.sube == 0))) & (m.empate == 0)
    n = len(m); w = int(m.gana.sum()); p = w / n; lo, hi = wilson(w, n); ev = p * PAGO - (1 - p)
    if n < 100: lect = "muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más)"
    elif lo > EQ: lect = "supera el equilibrio con margen estadístico"
    elif hi < EQ: lect = "por debajo del equilibrio"
    else: lect = "no se puede afirmar nada todavía"
    out = ["## Modelo de 30 minutos (en vivo)", "",
           "Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**", "",
           f"**Total:** {n} señales · acierto **{p*100:.1f}%** (rango {lo*100:.1f}% a {hi*100:.1f}%) · ganancia esperada {ev*100:+.1f}% por operación · equilibrio {EQ*100:.1f}% → {lect}.", "",
           "| Par | Señales | Acierto |", "|---|---|---|"]
    for par, g in m.groupby("par"): out.append(f"| {par} | {len(g)} | {g.gana.mean()*100:.1f}% |")
    out.append("")
    return out

def main():
    d = cargar()
    if d is None:
        txt = "# Informe\n\nTodavía no hay datos registrados.\n\n" + "\n".join(seccion_modelo()) + "\n"
        DATOS.mkdir(exist_ok=True); (DATOS / "informe.md").write_text(txt); print(txt); return
    dias = d.t_senal.str[:10].nunique(); desde, hasta = d.t_senal.min(), d.t_senal.max()
    filas = []
    for par, g in d.groupby("par"):
        for nom, nivel in GRUPOS:
            s = g[g.nivel >= nivel] if nivel < 3 else g[g.nivel == 3]
            n = len(s); w = int(s.gana.sum())
            filas.append(dict(par=par, grupo=nom, n=n, w=w))
    tot = []
    for nom, nivel in GRUPOS:
        s = d[d.nivel >= nivel] if nivel < 3 else d[d.nivel == 3]
        tot.append(dict(par="TODOS LOS PARES", grupo=nom, n=len(s), w=int(s.gana.sum())))
    T = pd.DataFrame(filas); A = pd.DataFrame(tot)
    valid = T[T.n >= MIN_N].copy()
    valid["p"] = [p_valor(w, n) for w, n in zip(valid.w, valid.n)]
    valid["ok"] = holm(list(valid.p)) if len(valid) else []
    T = T.merge(valid[["par", "grupo", "p", "ok"]], on=["par", "grupo"], how="left")

    def linea(r, corr=True):
        if r.n == 0: return f"| {r.par} | {r.n} | — | — | — | — |"
        p = r.w / r.n; lo, hi = wilson(r.w, r.n); ev = p * PAGO - (1 - p)
        if r.n < MIN_N: marca = "muy pocos datos"
        elif corr and r.get("ok") is True: marca = "**supera el equilibrio (no es azar)**"
        elif lo > EQ: marca = "supera el equilibrio, pero puede ser azar por probar varios pares"
        elif hi < EQ: marca = "por debajo del equilibrio"
        else: marca = "no se puede afirmar nada todavía"
        return f"| {r.par} | {r.n} | {p*100:.1f}% | {lo*100:.1f}% a {hi*100:.1f}% | {ev*100:+.1f}% | {marca} |"

    out = ["# Informe automático del escáner", "",
           f"Datos desde **{desde}** hasta **{hasta}** (UTC) · {dias} días con datos · {len(d):,} velas registradas · {int((d['dir']!=0).sum())} señales.".replace(",", "."), "",
           f"Equilibrio con pago {PAGO*100:.0f}%: **{EQ*100:.1f}%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.", "",
           "Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, "
           "algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.", ""]
    for nom, nivel in GRUPOS:
        out += [f"## {nom}", "", "| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |", "|---|---|---|---|---|---|"]
        sub = T[T.grupo == nom].sort_values("n", ascending=False)
        for _, r in sub.iterrows(): out.append(linea(r))
        out.append(linea(A[A.grupo == nom].iloc[0], corr=False)); out.append("")
    # chequeo de horario: en los datos de baja liquidez (cierre diario de los bancos) suelen aparecer resultados falsamente buenos
    out += ["## Chequeo por franja horaria (todas las señales, todos los pares)", "",
            "Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.", "",
            "| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |", "|---|---|---|---|"]
    sd = d[d["dir"] != 0]
    for a, b, tz in ((0, 6, "21:00 a 03:00"), (6, 13, "03:00 a 10:00"), (13, 21, "10:00 a 18:00"), (21, 24, "18:00 a 21:00")):
        s2 = sd[(sd.hora_utc >= a) & (sd.hora_utc < b)]
        out.append(f"| {a:02d}:00 a {b:02d}:00 | {tz} | {len(s2)} | " + (f"{s2.gana.mean()*100:.1f}%" if len(s2) else "—") + " |")
    out.append("")
    out += ["## Cuántas señales entran por día", ""]
    por_dia = d[d["dir"] != 0].groupby(["par"]).size() / max(dias, 1)
    out.append("Promedio de señales por día (todos los niveles): " + ", ".join(f"{k} {v:.1f}" for k, v in por_dia.items()) + f". **Total: {por_dia.sum():.1f} por día.**")
    out.append("")
    out.append("> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). "
               "No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.")
    out += seccion_modelo()
    txt = "\n".join(out) + "\n"
    DATOS.mkdir(exist_ok=True); (DATOS / "informe.md").write_text(txt); print(txt)

if __name__ == "__main__":
    main()
