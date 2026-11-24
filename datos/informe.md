# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-24 22:15** (UTC) · 16 días con datos · 14.571 velas registradas · 547 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 62 | 53.2% | 41.0% a 65.1% | +1.1% | no se puede afirmar nada todavía |
| GBP/JPY | 61 | 52.5% | 40.2% a 64.5% | -0.3% | no se puede afirmar nada todavía |
| EUR/JPY | 60 | 48.3% | 36.2% a 60.7% | -8.2% | no se puede afirmar nada todavía |
| EUR/GBP | 58 | 56.9% | 44.1% a 68.8% | +8.1% | no se puede afirmar nada todavía |
| AUD/USD | 56 | 33.9% | 22.9% a 47.0% | -35.5% | por debajo del equilibrio |
| GBP/USD | 56 | 46.4% | 34.0% a 59.3% | -11.8% | no se puede afirmar nada todavía |
| USD/CHF | 54 | 53.7% | 40.6% a 66.3% | +2.0% | no se puede afirmar nada todavía |
| EUR/USD | 51 | 41.2% | 28.8% a 54.8% | -21.8% | no se puede afirmar nada todavía |
| NZD/USD | 47 | 46.8% | 33.3% a 60.8% | -11.1% | no se puede afirmar nada todavía |
| USD/CAD | 42 | 57.1% | 42.2% a 70.9% | +8.6% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 547 | 49.0% | 44.8% a 53.2% | -6.9% | no se puede afirmar nada todavía |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 26 | 46.2% | 28.8% a 64.5% | -12.3% | muy pocos datos |
| AUD/USD | 23 | 39.1% | 22.2% a 59.2% | -25.7% | muy pocos datos |
| USD/CHF | 23 | 52.2% | 33.0% a 70.8% | -0.9% | muy pocos datos |
| EUR/JPY | 23 | 56.5% | 36.8% a 74.4% | +7.4% | muy pocos datos |
| USD/JPY | 23 | 60.9% | 40.8% a 77.8% | +15.7% | muy pocos datos |
| NZD/USD | 22 | 36.4% | 19.7% a 57.0% | -30.9% | muy pocos datos |
| GBP/USD | 21 | 38.1% | 20.8% a 59.1% | -27.6% | muy pocos datos |
| GBP/JPY | 19 | 57.9% | 36.3% a 76.9% | +10.0% | muy pocos datos |
| USD/CAD | 14 | 35.7% | 16.3% a 61.2% | -32.1% | muy pocos datos |
| EUR/GBP | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| TODOS LOS PARES | 204 | 47.5% | 40.8% a 54.4% | -9.7% | no se puede afirmar nada todavía |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 24 | 41.7% | 24.5% a 61.2% | -20.8% | muy pocos datos |
| USD/CHF | 21 | 47.6% | 28.3% a 67.6% | -9.5% | muy pocos datos |
| USD/JPY | 20 | 65.0% | 43.3% a 81.9% | +23.5% | muy pocos datos |
| EUR/JPY | 20 | 50.0% | 29.9% a 70.1% | -5.0% | muy pocos datos |
| GBP/USD | 19 | 31.6% | 15.4% a 54.0% | -40.0% | muy pocos datos |
| NZD/USD | 18 | 33.3% | 16.3% a 56.3% | -36.7% | muy pocos datos |
| AUD/USD | 17 | 47.1% | 26.2% a 69.0% | -10.6% | muy pocos datos |
| GBP/JPY | 14 | 50.0% | 26.8% a 73.2% | -5.0% | muy pocos datos |
| USD/CAD | 12 | 41.7% | 19.3% a 68.0% | -20.8% | muy pocos datos |
| EUR/GBP | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| TODOS LOS PARES | 175 | 45.7% | 38.5% a 53.1% | -13.1% | no se puede afirmar nada todavía |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 141 | 49.6% |
| 06:00 a 13:00 | 03:00 a 10:00 | 156 | 59.6% |
| 13:00 a 21:00 | 10:00 a 18:00 | 207 | 37.7% |
| 21:00 a 24:00 | 18:00 a 21:00 | 43 | 62.8% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.5, EUR/GBP 3.6, EUR/JPY 3.8, EUR/USD 3.2, GBP/JPY 3.8, GBP/USD 3.5, NZD/USD 2.9, USD/CAD 2.6, USD/CHF 3.4, USD/JPY 3.9. **Total: 34.2 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 138 señales · acierto **50.0%** (rango 41.8% a 58.2%) · ganancia esperada -5.0% por operación · equilibrio 52.6% → no se puede afirmar nada todavía.

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 19 | 57.9% |
| EUR/GBP | 17 | 52.9% |
| EUR/JPY | 10 | 50.0% |
| EUR/USD | 29 | 41.4% |
| GBP/JPY | 6 | 33.3% |
| GBP/USD | 22 | 72.7% |
| NZD/USD | 20 | 30.0% |
| USD/CAD | 4 | 25.0% |
| USD/CHF | 6 | 66.7% |
| USD/JPY | 5 | 60.0% |

