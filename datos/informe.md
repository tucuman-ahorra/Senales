# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-19 12:15** (UTC) · 13 días con datos · 11.467 velas registradas · 455 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/JPY | 50 | 46.0% | 33.0% a 59.6% | -12.6% | no se puede afirmar nada todavía |
| GBP/JPY | 49 | 53.1% | 39.4% a 66.3% | +0.8% | no se puede afirmar nada todavía |
| USD/JPY | 49 | 55.1% | 41.3% a 68.1% | +4.7% | no se puede afirmar nada todavía |
| GBP/USD | 48 | 43.8% | 30.7% a 57.7% | -16.9% | no se puede afirmar nada todavía |
| AUD/USD | 47 | 34.0% | 22.2% a 48.3% | -35.3% | por debajo del equilibrio |
| EUR/GBP | 45 | 57.8% | 43.3% a 71.0% | +9.8% | no se puede afirmar nada todavía |
| USD/CHF | 45 | 51.1% | 37.0% a 65.0% | -2.9% | no se puede afirmar nada todavía |
| EUR/USD | 44 | 40.9% | 27.7% a 55.6% | -22.3% | no se puede afirmar nada todavía |
| NZD/USD | 42 | 50.0% | 35.5% a 64.5% | -5.0% | no se puede afirmar nada todavía |
| USD/CAD | 36 | 58.3% | 42.2% a 72.9% | +10.8% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 455 | 48.8% | 44.2% a 53.4% | -7.3% | no se puede afirmar nada todavía |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 24 | 50.0% | 31.4% a 68.6% | -5.0% | muy pocos datos |
| AUD/USD | 21 | 42.9% | 24.5% a 63.5% | -18.6% | muy pocos datos |
| USD/JPY | 21 | 57.1% | 36.5% a 75.5% | +8.6% | muy pocos datos |
| NZD/USD | 21 | 38.1% | 20.8% a 59.1% | -27.6% | muy pocos datos |
| EUR/JPY | 20 | 50.0% | 29.9% a 70.1% | -5.0% | muy pocos datos |
| USD/CHF | 19 | 47.4% | 27.3% a 68.3% | -10.0% | muy pocos datos |
| GBP/USD | 19 | 31.6% | 15.4% a 54.0% | -40.0% | muy pocos datos |
| USD/CAD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| GBP/JPY | 11 | 54.5% | 28.0% a 78.7% | +3.6% | muy pocos datos |
| EUR/GBP | 9 | 55.6% | 26.7% a 81.1% | +5.6% | muy pocos datos |
| TODOS LOS PARES | 177 | 45.8% | 38.6% a 53.1% | -13.1% | no se puede afirmar nada todavía |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 22 | 45.5% | 26.9% a 65.3% | -13.6% | muy pocos datos |
| NZD/USD | 18 | 33.3% | 16.3% a 56.3% | -36.7% | muy pocos datos |
| USD/JPY | 18 | 61.1% | 38.6% a 79.7% | +16.1% | muy pocos datos |
| AUD/USD | 17 | 47.1% | 26.2% a 69.0% | -10.6% | muy pocos datos |
| USD/CHF | 17 | 41.2% | 21.6% a 64.0% | -21.8% | muy pocos datos |
| EUR/JPY | 17 | 41.2% | 21.6% a 64.0% | -21.8% | muy pocos datos |
| GBP/USD | 17 | 23.5% | 9.6% a 47.3% | -55.3% | muy pocos datos |
| USD/CAD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| EUR/GBP | 9 | 55.6% | 26.7% a 81.1% | +5.6% | muy pocos datos |
| GBP/JPY | 8 | 37.5% | 13.7% a 69.4% | -28.7% | muy pocos datos |
| TODOS LOS PARES | 153 | 42.5% | 34.9% a 50.4% | -19.3% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 122 | 49.2% |
| 06:00 a 13:00 | 03:00 a 10:00 | 125 | 60.8% |
| 13:00 a 21:00 | 10:00 a 18:00 | 172 | 38.4% |
| 21:00 a 24:00 | 18:00 a 21:00 | 36 | 55.6% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.6, EUR/GBP 3.5, EUR/JPY 3.8, EUR/USD 3.4, GBP/JPY 3.8, GBP/USD 3.7, NZD/USD 3.2, USD/CAD 2.8, USD/CHF 3.5, USD/JPY 3.8. **Total: 35.0 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 107 señales · acierto **52.3%** (rango 43.0% a 61.6%) · ganancia esperada -0.6% por operación · equilibrio 52.6% → no se puede afirmar nada todavía.

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 15 | 60.0% |
| EUR/GBP | 11 | 72.7% |
| EUR/JPY | 8 | 62.5% |
| EUR/USD | 23 | 39.1% |
| GBP/JPY | 5 | 40.0% |
| GBP/USD | 19 | 73.7% |
| NZD/USD | 14 | 28.6% |
| USD/CAD | 4 | 25.0% |
| USD/CHF | 5 | 60.0% |
| USD/JPY | 3 | 33.3% |

