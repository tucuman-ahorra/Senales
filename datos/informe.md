# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-11 04:45** (UTC) · 7 días con datos · 5.638 velas registradas · 231 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 30 | 46.7% | 30.2% a 63.9% | -11.3% | no se puede afirmar nada todavía |
| USD/CHF | 27 | 44.4% | 27.6% a 62.7% | -15.6% | muy pocos datos |
| GBP/USD | 25 | 32.0% | 17.2% a 51.6% | -39.2% | muy pocos datos |
| EUR/JPY | 24 | 50.0% | 31.4% a 68.6% | -5.0% | muy pocos datos |
| NZD/USD | 23 | 43.5% | 25.6% a 63.2% | -17.4% | muy pocos datos |
| EUR/USD | 22 | 36.4% | 19.7% a 57.0% | -30.9% | muy pocos datos |
| GBP/JPY | 22 | 50.0% | 30.7% a 69.3% | -5.0% | muy pocos datos |
| AUD/USD | 20 | 25.0% | 11.2% a 46.9% | -52.5% | muy pocos datos |
| EUR/GBP | 20 | 50.0% | 29.9% a 70.1% | -5.0% | muy pocos datos |
| USD/CAD | 18 | 50.0% | 29.0% a 71.0% | -5.0% | muy pocos datos |
| TODOS LOS PARES | 231 | 42.9% | 36.6% a 49.3% | -18.6% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| NZD/USD | 15 | 33.3% | 15.2% a 58.3% | -36.7% | muy pocos datos |
| EUR/USD | 15 | 46.7% | 24.8% a 69.9% | -11.3% | muy pocos datos |
| USD/JPY | 15 | 40.0% | 19.8% a 64.3% | -24.0% | muy pocos datos |
| USD/CHF | 12 | 41.7% | 19.3% a 68.0% | -20.8% | muy pocos datos |
| EUR/JPY | 11 | 54.5% | 28.0% a 78.7% | +3.6% | muy pocos datos |
| AUD/USD | 11 | 27.3% | 9.7% a 56.6% | -48.2% | muy pocos datos |
| USD/CAD | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| GBP/USD | 8 | 12.5% | 2.2% a 47.1% | -76.2% | muy pocos datos |
| GBP/JPY | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 109 | 39.4% | 30.8% a 48.8% | -25.0% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 14 | 42.9% | 21.4% a 67.4% | -18.6% | muy pocos datos |
| NZD/USD | 13 | 23.1% | 8.2% a 50.3% | -56.2% | muy pocos datos |
| USD/JPY | 12 | 41.7% | 19.3% a 68.0% | -20.8% | muy pocos datos |
| USD/CHF | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| EUR/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| USD/CAD | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| GBP/USD | 8 | 12.5% | 2.2% a 47.1% | -76.2% | muy pocos datos |
| AUD/USD | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| GBP/JPY | 6 | 16.7% | 3.0% a 56.4% | -68.3% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 93 | 36.6% | 27.5% a 46.7% | -30.5% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 70 | 42.9% |
| 06:00 a 13:00 | 03:00 a 10:00 | 62 | 53.2% |
| 13:00 a 21:00 | 10:00 a 18:00 | 92 | 33.7% |
| 21:00 a 24:00 | 18:00 a 21:00 | 7 | 71.4% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 2.9, EUR/GBP 2.9, EUR/JPY 3.4, EUR/USD 3.1, GBP/JPY 3.1, GBP/USD 3.6, NZD/USD 3.3, USD/CAD 2.6, USD/CHF 3.9, USD/JPY 4.3. **Total: 33.0 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 63 señales · acierto **46.0%** (rango 34.3% a 58.2%) · ganancia esperada -12.5% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 9 | 44.4% |
| EUR/GBP | 7 | 85.7% |
| EUR/JPY | 1 | 100.0% |
| EUR/USD | 14 | 35.7% |
| GBP/JPY | 1 | 0.0% |
| GBP/USD | 11 | 54.5% |
| NZD/USD | 13 | 30.8% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 2 | 100.0% |
| USD/JPY | 2 | 50.0% |

