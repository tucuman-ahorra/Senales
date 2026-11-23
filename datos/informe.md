# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-23 15:45** (UTC) · 15 días con datos · 13.387 velas registradas · 513 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 60 | 53.3% | 40.9% a 65.4% | +1.3% | no se puede afirmar nada todavía |
| GBP/JPY | 56 | 53.6% | 40.7% a 66.0% | +1.8% | no se puede afirmar nada todavía |
| EUR/JPY | 54 | 44.4% | 32.0% a 57.6% | -15.6% | no se puede afirmar nada todavía |
| AUD/USD | 54 | 31.5% | 20.7% a 44.7% | -40.2% | por debajo del equilibrio |
| EUR/GBP | 53 | 56.6% | 43.3% a 69.0% | +7.5% | no se puede afirmar nada todavía |
| GBP/USD | 53 | 45.3% | 32.7% a 58.5% | -14.0% | no se puede afirmar nada todavía |
| USD/CHF | 51 | 51.0% | 37.7% a 64.1% | -3.1% | no se puede afirmar nada todavía |
| EUR/USD | 48 | 39.6% | 27.0% a 53.7% | -24.8% | no se puede afirmar nada todavía |
| NZD/USD | 46 | 45.7% | 32.2% a 59.8% | -13.3% | no se puede afirmar nada todavía |
| USD/CAD | 38 | 55.3% | 39.7% a 69.9% | +5.0% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 513 | 47.6% | 43.3% a 51.9% | -9.6% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 25 | 48.0% | 30.0% a 66.5% | -8.8% | muy pocos datos |
| AUD/USD | 23 | 39.1% | 22.2% a 59.2% | -25.7% | muy pocos datos |
| USD/JPY | 23 | 60.9% | 40.8% a 77.8% | +15.7% | muy pocos datos |
| NZD/USD | 22 | 36.4% | 19.7% a 57.0% | -30.9% | muy pocos datos |
| USD/CHF | 22 | 50.0% | 30.7% a 69.3% | -5.0% | muy pocos datos |
| EUR/JPY | 21 | 52.4% | 32.4% a 71.7% | -0.5% | muy pocos datos |
| GBP/USD | 21 | 38.1% | 20.8% a 59.1% | -27.6% | muy pocos datos |
| GBP/JPY | 16 | 56.2% | 33.2% a 76.9% | +6.9% | muy pocos datos |
| USD/CAD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| EUR/GBP | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| TODOS LOS PARES | 195 | 46.7% | 39.8% a 53.7% | -11.3% | no se puede afirmar nada todavía |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 23 | 43.5% | 25.6% a 63.2% | -17.4% | muy pocos datos |
| USD/JPY | 20 | 65.0% | 43.3% a 81.9% | +23.5% | muy pocos datos |
| USD/CHF | 20 | 45.0% | 25.8% a 65.8% | -14.5% | muy pocos datos |
| GBP/USD | 19 | 31.6% | 15.4% a 54.0% | -40.0% | muy pocos datos |
| NZD/USD | 18 | 33.3% | 16.3% a 56.3% | -36.7% | muy pocos datos |
| EUR/JPY | 18 | 44.4% | 24.6% a 66.3% | -15.6% | muy pocos datos |
| AUD/USD | 17 | 47.1% | 26.2% a 69.0% | -10.6% | muy pocos datos |
| GBP/JPY | 11 | 45.5% | 21.3% a 72.0% | -13.6% | muy pocos datos |
| EUR/GBP | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| USD/CAD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| TODOS LOS PARES | 166 | 44.6% | 37.2% a 52.2% | -15.3% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 128 | 48.4% |
| 06:00 a 13:00 | 03:00 a 10:00 | 144 | 58.3% |
| 13:00 a 21:00 | 10:00 a 18:00 | 203 | 37.4% |
| 21:00 a 24:00 | 18:00 a 21:00 | 38 | 57.9% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.6, EUR/GBP 3.5, EUR/JPY 3.6, EUR/USD 3.2, GBP/JPY 3.7, GBP/USD 3.5, NZD/USD 3.1, USD/CAD 2.5, USD/CHF 3.4, USD/JPY 4.0. **Total: 34.2 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 123 señales · acierto **48.8%** (rango 40.1% a 57.5%) · ganancia esperada -7.3% por operación · equilibrio 52.6% → no se puede afirmar nada todavía.

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 17 | 58.8% |
| EUR/GBP | 16 | 50.0% |
| EUR/JPY | 10 | 50.0% |
| EUR/USD | 26 | 42.3% |
| GBP/JPY | 6 | 33.3% |
| GBP/USD | 19 | 73.7% |
| NZD/USD | 16 | 25.0% |
| USD/CAD | 4 | 25.0% |
| USD/CHF | 5 | 60.0% |
| USD/JPY | 4 | 50.0% |

