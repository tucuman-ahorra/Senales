# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-25 15:45** (UTC) · 17 días con datos · 15.241 velas registradas · 570 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 64 | 54.7% | 42.6% a 66.3% | +3.9% | no se puede afirmar nada todavía |
| GBP/JPY | 64 | 54.7% | 42.6% a 66.3% | +3.9% | no se puede afirmar nada todavía |
| EUR/GBP | 63 | 58.7% | 46.4% a 70.0% | +11.6% | no se puede afirmar nada todavía |
| EUR/JPY | 62 | 50.0% | 37.9% a 62.1% | -5.0% | no se puede afirmar nada todavía |
| AUD/USD | 59 | 37.3% | 26.1% a 50.0% | -29.2% | por debajo del equilibrio |
| GBP/USD | 58 | 46.6% | 34.3% a 59.2% | -11.6% | no se puede afirmar nada todavía |
| USD/CHF | 56 | 55.4% | 42.4% a 67.6% | +5.2% | no se puede afirmar nada todavía |
| EUR/USD | 52 | 40.4% | 28.2% a 53.9% | -23.3% | no se puede afirmar nada todavía |
| NZD/USD | 48 | 45.8% | 32.6% a 59.7% | -12.9% | no se puede afirmar nada todavía |
| USD/CAD | 44 | 56.8% | 42.2% a 70.3% | +8.0% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 570 | 50.2% | 46.1% a 54.3% | -4.7% | no se puede afirmar nada todavía |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 26 | 46.2% | 28.8% a 64.5% | -12.3% | muy pocos datos |
| AUD/USD | 24 | 41.7% | 24.5% a 61.2% | -20.8% | muy pocos datos |
| EUR/JPY | 24 | 58.3% | 38.8% a 75.5% | +10.8% | muy pocos datos |
| USD/CHF | 23 | 52.2% | 33.0% a 70.8% | -0.9% | muy pocos datos |
| USD/JPY | 23 | 60.9% | 40.8% a 77.8% | +15.7% | muy pocos datos |
| NZD/USD | 22 | 36.4% | 19.7% a 57.0% | -30.9% | muy pocos datos |
| GBP/USD | 21 | 38.1% | 20.8% a 59.1% | -27.6% | muy pocos datos |
| GBP/JPY | 21 | 61.9% | 40.9% a 79.2% | +17.6% | muy pocos datos |
| USD/CAD | 14 | 35.7% | 16.3% a 61.2% | -32.1% | muy pocos datos |
| EUR/GBP | 13 | 53.8% | 29.1% a 76.8% | +2.3% | muy pocos datos |
| TODOS LOS PARES | 211 | 48.8% | 42.2% a 55.5% | -7.3% | no se puede afirmar nada todavía |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 24 | 41.7% | 24.5% a 61.2% | -20.8% | muy pocos datos |
| EUR/JPY | 21 | 52.4% | 32.4% a 71.7% | -0.5% | muy pocos datos |
| USD/CHF | 21 | 47.6% | 28.3% a 67.6% | -9.5% | muy pocos datos |
| USD/JPY | 20 | 65.0% | 43.3% a 81.9% | +23.5% | muy pocos datos |
| GBP/USD | 19 | 31.6% | 15.4% a 54.0% | -40.0% | muy pocos datos |
| AUD/USD | 18 | 50.0% | 29.0% a 71.0% | -5.0% | muy pocos datos |
| NZD/USD | 18 | 33.3% | 16.3% a 56.3% | -36.7% | muy pocos datos |
| GBP/JPY | 16 | 56.2% | 33.2% a 76.9% | +6.9% | muy pocos datos |
| EUR/GBP | 13 | 53.8% | 29.1% a 76.8% | +2.3% | muy pocos datos |
| USD/CAD | 12 | 41.7% | 19.3% a 68.0% | -20.8% | muy pocos datos |
| TODOS LOS PARES | 182 | 47.3% | 40.1% a 54.5% | -10.2% | no se puede afirmar nada todavía |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 151 | 51.0% |
| 06:00 a 13:00 | 03:00 a 10:00 | 163 | 60.1% |
| 13:00 a 21:00 | 10:00 a 18:00 | 211 | 38.9% |
| 21:00 a 24:00 | 18:00 a 21:00 | 45 | 64.4% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.5, EUR/GBP 3.7, EUR/JPY 3.6, EUR/USD 3.1, GBP/JPY 3.8, GBP/USD 3.4, NZD/USD 2.8, USD/CAD 2.6, USD/CHF 3.3, USD/JPY 3.8. **Total: 33.5 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 147 señales · acierto **50.3%** (rango 42.4% a 58.3%) · ganancia esperada -4.4% por operación · equilibrio 52.6% → no se puede afirmar nada todavía.

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 22 | 59.1% |
| EUR/GBP | 18 | 55.6% |
| EUR/JPY | 12 | 50.0% |
| EUR/USD | 31 | 38.7% |
| GBP/JPY | 6 | 33.3% |
| GBP/USD | 23 | 73.9% |
| NZD/USD | 20 | 30.0% |
| USD/CAD | 4 | 25.0% |
| USD/CHF | 6 | 66.7% |
| USD/JPY | 5 | 60.0% |

