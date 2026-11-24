# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-24 10:15** (UTC) · 16 días con datos · 14.093 velas registradas · 539 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 62 | 53.2% | 41.0% a 65.1% | +1.1% | no se puede afirmar nada todavía |
| GBP/JPY | 60 | 53.3% | 40.9% a 65.4% | +1.3% | no se puede afirmar nada todavía |
| EUR/JPY | 59 | 47.5% | 35.3% a 60.0% | -9.8% | no se puede afirmar nada todavía |
| EUR/GBP | 56 | 57.1% | 44.1% a 69.2% | +8.6% | no se puede afirmar nada todavía |
| GBP/USD | 56 | 46.4% | 34.0% a 59.3% | -11.8% | no se puede afirmar nada todavía |
| AUD/USD | 55 | 32.7% | 21.8% a 45.9% | -37.8% | por debajo del equilibrio |
| USD/CHF | 53 | 52.8% | 39.7% a 65.6% | +0.4% | no se puede afirmar nada todavía |
| EUR/USD | 51 | 41.2% | 28.8% a 54.8% | -21.8% | no se puede afirmar nada todavía |
| NZD/USD | 47 | 46.8% | 33.3% a 60.8% | -11.1% | no se puede afirmar nada todavía |
| USD/CAD | 40 | 57.5% | 42.2% a 71.5% | +9.2% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 539 | 48.8% | 44.6% a 53.0% | -7.3% | no se puede afirmar nada todavía |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 26 | 46.2% | 28.8% a 64.5% | -12.3% | muy pocos datos |
| AUD/USD | 23 | 39.1% | 22.2% a 59.2% | -25.7% | muy pocos datos |
| USD/JPY | 23 | 60.9% | 40.8% a 77.8% | +15.7% | muy pocos datos |
| USD/CHF | 22 | 50.0% | 30.7% a 69.3% | -5.0% | muy pocos datos |
| NZD/USD | 22 | 36.4% | 19.7% a 57.0% | -30.9% | muy pocos datos |
| EUR/JPY | 22 | 54.5% | 34.7% a 73.1% | +3.6% | muy pocos datos |
| GBP/USD | 21 | 38.1% | 20.8% a 59.1% | -27.6% | muy pocos datos |
| GBP/JPY | 18 | 61.1% | 38.6% a 79.7% | +16.1% | muy pocos datos |
| USD/CAD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| EUR/GBP | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| TODOS LOS PARES | 199 | 47.2% | 40.4% a 54.2% | -10.3% | no se puede afirmar nada todavía |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 24 | 41.7% | 24.5% a 61.2% | -20.8% | muy pocos datos |
| USD/JPY | 20 | 65.0% | 43.3% a 81.9% | +23.5% | muy pocos datos |
| USD/CHF | 20 | 45.0% | 25.8% a 65.8% | -14.5% | muy pocos datos |
| EUR/JPY | 19 | 47.4% | 27.3% a 68.3% | -10.0% | muy pocos datos |
| GBP/USD | 19 | 31.6% | 15.4% a 54.0% | -40.0% | muy pocos datos |
| NZD/USD | 18 | 33.3% | 16.3% a 56.3% | -36.7% | muy pocos datos |
| AUD/USD | 17 | 47.1% | 26.2% a 69.0% | -10.6% | muy pocos datos |
| GBP/JPY | 13 | 53.8% | 29.1% a 76.8% | +2.3% | muy pocos datos |
| EUR/GBP | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| USD/CAD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| TODOS LOS PARES | 170 | 45.3% | 38.0% a 52.8% | -13.9% | no se puede afirmar nada todavía |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 141 | 49.6% |
| 06:00 a 13:00 | 03:00 a 10:00 | 152 | 59.2% |
| 13:00 a 21:00 | 10:00 a 18:00 | 203 | 37.4% |
| 21:00 a 24:00 | 18:00 a 21:00 | 43 | 62.8% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.4, EUR/GBP 3.5, EUR/JPY 3.7, EUR/USD 3.2, GBP/JPY 3.8, GBP/USD 3.5, NZD/USD 2.9, USD/CAD 2.5, USD/CHF 3.3, USD/JPY 3.9. **Total: 33.7 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 131 señales · acierto **50.4%** (rango 41.9% a 58.8%) · ganancia esperada -4.3% por operación · equilibrio 52.6% → no se puede afirmar nada todavía.

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 18 | 55.6% |
| EUR/GBP | 17 | 52.9% |
| EUR/JPY | 10 | 50.0% |
| EUR/USD | 27 | 44.4% |
| GBP/JPY | 6 | 33.3% |
| GBP/USD | 21 | 71.4% |
| NZD/USD | 17 | 29.4% |
| USD/CAD | 4 | 25.0% |
| USD/CHF | 6 | 66.7% |
| USD/JPY | 5 | 60.0% |

