# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-18 04:15** (UTC) · 12 días con datos · 10.221 velas registradas · 417 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 47 | 53.2% | 39.2% a 66.7% | +1.1% | no se puede afirmar nada todavía |
| EUR/JPY | 47 | 48.9% | 35.3% a 62.8% | -7.0% | no se puede afirmar nada todavía |
| GBP/JPY | 46 | 52.2% | 38.1% a 65.9% | -0.9% | no se puede afirmar nada todavía |
| GBP/USD | 44 | 40.9% | 27.7% a 55.6% | -22.3% | no se puede afirmar nada todavía |
| EUR/USD | 42 | 40.5% | 27.0% a 55.5% | -23.1% | no se puede afirmar nada todavía |
| USD/CHF | 41 | 46.3% | 32.1% a 61.3% | -12.0% | no se puede afirmar nada todavía |
| AUD/USD | 40 | 32.5% | 20.1% a 48.0% | -38.2% | por debajo del equilibrio |
| EUR/GBP | 39 | 56.4% | 41.0% a 70.7% | +7.2% | no se puede afirmar nada todavía |
| NZD/USD | 37 | 51.4% | 35.9% a 66.6% | -2.4% | no se puede afirmar nada todavía |
| USD/CAD | 34 | 58.8% | 42.2% a 73.6% | +11.8% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 417 | 48.0% | 43.2% a 52.8% | -8.9% | no se puede afirmar nada todavía |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 23 | 47.8% | 29.2% a 67.0% | -9.1% | muy pocos datos |
| AUD/USD | 19 | 36.8% | 19.1% a 59.0% | -30.0% | muy pocos datos |
| USD/JPY | 19 | 52.6% | 31.7% a 72.7% | -0.0% | muy pocos datos |
| NZD/USD | 19 | 42.1% | 23.1% a 63.7% | -20.0% | muy pocos datos |
| GBP/USD | 17 | 23.5% | 9.6% a 47.3% | -55.3% | muy pocos datos |
| EUR/JPY | 17 | 58.8% | 36.0% a 78.4% | +11.8% | muy pocos datos |
| USD/CHF | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| USD/CAD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| GBP/JPY | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| EUR/GBP | 7 | 57.1% | 25.0% a 84.2% | +8.6% | muy pocos datos |
| TODOS LOS PARES | 159 | 43.4% | 35.9% a 51.2% | -17.5% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 21 | 42.9% | 24.5% a 63.5% | -18.6% | muy pocos datos |
| NZD/USD | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| USD/JPY | 16 | 56.2% | 33.2% a 76.9% | +6.9% | muy pocos datos |
| AUD/USD | 15 | 40.0% | 19.8% a 64.3% | -24.0% | muy pocos datos |
| GBP/USD | 15 | 13.3% | 3.7% a 37.9% | -74.7% | muy pocos datos |
| USD/CHF | 14 | 28.6% | 11.7% a 54.6% | -45.7% | muy pocos datos |
| EUR/JPY | 14 | 50.0% | 26.8% a 73.2% | -5.0% | muy pocos datos |
| USD/CAD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| EUR/GBP | 7 | 57.1% | 25.0% a 84.2% | +8.6% | muy pocos datos |
| GBP/JPY | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| TODOS LOS PARES | 135 | 39.3% | 31.4% a 47.7% | -25.4% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 112 | 47.3% |
| 06:00 a 13:00 | 03:00 a 10:00 | 106 | 61.3% |
| 13:00 a 21:00 | 10:00 a 18:00 | 163 | 38.0% |
| 21:00 a 24:00 | 18:00 a 21:00 | 36 | 55.6% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.3, EUR/GBP 3.2, EUR/JPY 3.9, EUR/USD 3.5, GBP/JPY 3.8, GBP/USD 3.7, NZD/USD 3.1, USD/CAD 2.8, USD/CHF 3.4, USD/JPY 3.9. **Total: 34.8 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 92 señales · acierto **50.0%** (rango 40.0% a 60.0%) · ganancia esperada -5.0% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 13 | 61.5% |
| EUR/GBP | 9 | 77.8% |
| EUR/JPY | 5 | 60.0% |
| EUR/USD | 20 | 40.0% |
| GBP/JPY | 4 | 25.0% |
| GBP/USD | 16 | 68.8% |
| NZD/USD | 14 | 28.6% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 5 | 60.0% |
| USD/JPY | 3 | 33.3% |

