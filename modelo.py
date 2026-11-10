"""Modelo combinado de 30 minutos (árboles de decisión exportados de scikit-learn; ver modelo30.json).
Calcula, para cada vela cerrada de 30 min, la probabilidad de que la PRÓXIMA vela suba.
Los datos de entrada son un DataFrame con columnas o,h,l,c e índice = inicio de la vela (UTC)."""
import json
from pathlib import Path
import numpy as np, pandas as pd

M = json.loads((Path(__file__).resolve().parent / "modelo30.json").read_text())
PARES = ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD", "USD/CAD", "NZD/USD", "EUR/GBP", "EUR/JPY", "GBP/JPY"]
CORTE = 0.0445        # confianza mínima: |p - 0,5| >= CORTE (aprox. el 2% de velas más seguras)
HORA_MAX = 21         # no se opera si la vela de entrada abre desde las 21:00 UTC (cierre diario)
MIN_VELAS = 130       # el modelo necesita historia (z de 80 velas, volatilidad de 100 velas, etc.)

def _rsi(c, n=14):
    d = c.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d).clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / (dn + 1e-12))

def features(g, par):
    o, h, l, c = g.o, g.h, g.l, g.c
    f = pd.DataFrame(index=g.index)
    f["z20"] = (c - c.rolling(20).mean()) / c.rolling(20).std(ddof=1)
    f["z80"] = (c - c.rolling(80).mean()) / c.rolling(80).std(ddof=1)
    f["rsi"] = _rsi(c)
    ll, hh = l.rolling(14).min(), h.rolling(14).max()
    f["st"] = 100 * (c - ll) / (hh - ll + 1e-12)
    atr = (h - l).rolling(14).mean()
    f["vr"] = atr / atr.rolling(100).mean()
    f["ret1"] = (c - o) / atr
    f["ret1p"] = f.ret1.shift(1); f["ret2p"] = f.ret1.shift(2)
    f["ret3"] = (c - c.shift(3)) / atr; f["ret6"] = (c - c.shift(6)) / atr
    f["ema50"] = (c - c.ewm(span=50).mean()) / atr
    rng = (h - l) + 1e-12
    f["wsup"] = (h - np.maximum(o, c)) / rng; f["winf"] = (np.minimum(o, c) - l) / rng
    f["rng"] = (h - l) / atr
    hora = (g.index + pd.Timedelta(minutes=30)).hour
    f["hs"] = np.sin(2 * np.pi * hora / 24); f["hc"] = np.cos(2 * np.pi * hora / 24)
    f["dow"] = g.index.dayofweek
    for p in PARES:
        f["p_" + p.replace("/", "")] = int(p == par)
    f["hora"] = hora
    return f

def probabilidad(X):
    """X: matriz (n, 27) en el orden de M['F']. Devuelve la probabilidad de que suba la vela siguiente."""
    s = np.full(len(X), M["base"], dtype=float)
    for arbol in M["trees"]:
        a = np.array(arbol, dtype=float)
        feat, thr, izq, der, val = a[:, 0].astype(int), a[:, 1], a[:, 2].astype(int), a[:, 3].astype(int), a[:, 4]
        idx = np.zeros(len(X), dtype=int)
        for _ in range(8):
            f = feat[idx]; hoja = f < 0
            if hoja.all(): break
            x = X[np.arange(len(X)), np.where(hoja, 0, f)]
            idx = np.where(hoja, idx, np.where(x <= thr[idx], izq[idx], der[idx]))
        s += val[idx]
    return 1 / (1 + np.exp(-s))

def evaluar(g, par):
    """Devuelve un DataFrame con p, dir (1 sube / -1 baja), conf y sen (¿señal del modelo?) por cada vela de g."""
    f = features(g, par)
    ok = ~f[M["F"]].isna().any(axis=1)
    out = pd.DataFrame(index=g.index, data={"p": np.nan, "dir": 0, "conf": np.nan, "sen": False, "hora": f.hora})
    if ok.sum() == 0: return out
    p = probabilidad(f.loc[ok, M["F"]].values.astype(float))
    out.loc[ok, "p"] = p
    out.loc[ok, "dir"] = np.where(p >= 0.5, 1, -1)
    out.loc[ok, "conf"] = np.abs(p - 0.5)
    out["sen"] = (out.conf >= CORTE) & (out.hora < HORA_MAX)
    return out
