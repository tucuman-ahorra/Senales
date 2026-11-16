# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-16 19:15** (UTC) · 10 días con datos · 8.952 velas registradas · 380 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 43 | 53.5% | 38.9% a 67.5% | +1.6% | no se puede afirmar nada todavía |
| GBP/USD | 42 | 38.1% | 25.0% a 53.2% | -27.6% | no se puede afirmar nada todavía |
| GBP/JPY | 41 | 51.2% | 36.5% a 65.7% | -2.7% | no se puede afirmar nada todavía |
| EUR/JPY | 41 | 46.3% | 32.1% a 61.3% | -12.0% | no se puede afirmar nada todavía |
| EUR/USD | 40 | 37.5% | 24.2% a 53.0% | -28.7% | no se puede afirmar nada todavía |
| USD/CHF | 40 | 47.5% | 32.9% a 62.5% | -9.8% | no se puede afirmar nada todavía |
| AUD/USD | 37 | 29.7% | 17.5% a 45.8% | -43.5% | por debajo del equilibrio |
| EUR/GBP | 33 | 54.5% | 38.0% a 70.2% | +3.6% | no se puede afirmar nada todavía |
| NZD/USD | 33 | 51.5% | 35.2% a 67.5% | -2.1% | no se puede afirmar nada todavía |
| USD/CAD | 30 | 56.7% | 39.2% a 72.6% | +7.7% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 380 | 46.3% | 41.4% a 51.3% | -12.0% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 23 | 47.8% | 29.2% a 67.0% | -9.1% | muy pocos datos |
| AUD/USD | 19 | 36.8% | 19.1% a 59.0% | -30.0% | muy pocos datos |
| NZD/USD | 19 | 42.1% | 23.1% a 63.7% | -20.0% | muy pocos datos |
| USD/JPY | 18 | 50.0% | 29.0% a 71.0% | -5.0% | muy pocos datos |
| GBP/USD | 17 | 23.5% | 9.6% a 47.3% | -55.3% | muy pocos datos |
| USD/CHF | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| EUR/JPY | 14 | 50.0% | 26.8% a 73.2% | -5.0% | muy pocos datos |
| USD/CAD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| GBP/JPY | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| EUR/GBP | 5 | 80.0% | 37.6% a 96.4% | +52.0% | muy pocos datos |
| TODOS LOS PARES | 153 | 42.5% | 34.9% a 50.4% | -19.3% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 21 | 42.9% | 24.5% a 63.5% | -18.6% | muy pocos datos |
| NZD/USD | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| USD/JPY | 15 | 53.3% | 30.1% a 75.2% | +1.3% | muy pocos datos |
| AUD/USD | 15 | 40.0% | 19.8% a 64.3% | -24.0% | muy pocos datos |
| GBP/USD | 15 | 13.3% | 3.7% a 37.9% | -74.7% | muy pocos datos |
| USD/CHF | 14 | 28.6% | 11.7% a 54.6% | -45.7% | muy pocos datos |
| EUR/JPY | 12 | 41.7% | 19.3% a 68.0% | -20.8% | muy pocos datos |
| USD/CAD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| GBP/JPY | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| EUR/GBP | 5 | 80.0% | 37.6% a 96.4% | +52.0% | muy pocos datos |
| TODOS LOS PARES | 130 | 38.5% | 30.5% a 47.0% | -26.9% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 100 | 45.0% |
| 06:00 a 13:00 | 03:00 a 10:00 | 95 | 61.1% |
| 13:00 a 21:00 | 10:00 a 18:00 | 157 | 36.3% |
| 21:00 a 24:00 | 18:00 a 21:00 | 28 | 57.1% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.7, EUR/GBP 3.3, EUR/JPY 4.1, EUR/USD 4.0, GBP/JPY 4.1, GBP/USD 4.2, NZD/USD 3.3, USD/CAD 3.0, USD/CHF 4.0, USD/JPY 4.3. **Total: 38.0 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 79 señales · acierto **50.6%** (rango 39.8% a 61.4%) · ganancia esperada -3.8% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 11 | 54.5% |
| EUR/GBP | 9 | 77.8% |
| EUR/JPY | 2 | 100.0% |
| EUR/USD | 19 | 42.1% |
| GBP/JPY | 1 | 0.0% |
| GBP/USD | 15 | 66.7% |
| NZD/USD | 13 | 30.8% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 4 | 50.0% |
| USD/JPY | 2 | 50.0% |

