# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-18 15:45** (UTC) · 12 días con datos · 10.681 velas registradas · 429 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| GBP/JPY | 47 | 51.1% | 37.2% a 64.7% | -3.0% | no se puede afirmar nada todavía |
| EUR/JPY | 47 | 48.9% | 35.3% a 62.8% | -7.0% | no se puede afirmar nada todavía |
| USD/JPY | 47 | 53.2% | 39.2% a 66.7% | +1.1% | no se puede afirmar nada todavía |
| GBP/USD | 45 | 42.2% | 29.0% a 56.7% | -19.8% | no se puede afirmar nada todavía |
| USD/CHF | 43 | 48.8% | 34.6% a 63.2% | -7.2% | no se puede afirmar nada todavía |
| AUD/USD | 43 | 30.2% | 18.6% a 45.1% | -42.6% | por debajo del equilibrio |
| EUR/USD | 42 | 40.5% | 27.0% a 55.5% | -23.1% | no se puede afirmar nada todavía |
| EUR/GBP | 41 | 56.1% | 41.0% a 70.1% | +6.6% | no se puede afirmar nada todavía |
| NZD/USD | 38 | 50.0% | 34.8% a 65.2% | -5.0% | no se puede afirmar nada todavía |
| USD/CAD | 36 | 58.3% | 42.2% a 72.9% | +10.8% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 429 | 47.8% | 43.1% a 52.5% | -9.2% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 23 | 47.8% | 29.2% a 67.0% | -9.1% | muy pocos datos |
| AUD/USD | 19 | 36.8% | 19.1% a 59.0% | -30.0% | muy pocos datos |
| USD/JPY | 19 | 52.6% | 31.7% a 72.7% | -0.0% | muy pocos datos |
| NZD/USD | 19 | 42.1% | 23.1% a 63.7% | -20.0% | muy pocos datos |
| USD/CHF | 18 | 44.4% | 24.6% a 66.3% | -15.6% | muy pocos datos |
| GBP/USD | 18 | 27.8% | 12.5% a 50.9% | -47.2% | muy pocos datos |
| EUR/JPY | 17 | 58.8% | 36.0% a 78.4% | +11.8% | muy pocos datos |
| USD/CAD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| GBP/JPY | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| EUR/GBP | 7 | 57.1% | 25.0% a 84.2% | +8.6% | muy pocos datos |
| TODOS LOS PARES | 162 | 44.4% | 37.0% a 52.1% | -15.6% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 21 | 42.9% | 24.5% a 63.5% | -18.6% | muy pocos datos |
| GBP/USD | 16 | 18.8% | 6.6% a 43.0% | -64.4% | muy pocos datos |
| USD/JPY | 16 | 56.2% | 33.2% a 76.9% | +6.9% | muy pocos datos |
| NZD/USD | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| USD/CHF | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| AUD/USD | 15 | 40.0% | 19.8% a 64.3% | -24.0% | muy pocos datos |
| EUR/JPY | 14 | 50.0% | 26.8% a 73.2% | -5.0% | muy pocos datos |
| USD/CAD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| EUR/GBP | 7 | 57.1% | 25.0% a 84.2% | +8.6% | muy pocos datos |
| GBP/JPY | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| TODOS LOS PARES | 138 | 40.6% | 32.7% a 48.9% | -22.9% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 112 | 47.3% |
| 06:00 a 13:00 | 03:00 a 10:00 | 112 | 61.6% |
| 13:00 a 21:00 | 10:00 a 18:00 | 169 | 37.3% |
| 21:00 a 24:00 | 18:00 a 21:00 | 36 | 55.6% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.6, EUR/GBP 3.4, EUR/JPY 3.9, EUR/USD 3.5, GBP/JPY 3.9, GBP/USD 3.8, NZD/USD 3.2, USD/CAD 3.0, USD/CHF 3.6, USD/JPY 3.9. **Total: 35.8 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 100 señales · acierto **52.0%** (rango 42.3% a 61.5%) · ganancia esperada -1.2% por operación · equilibrio 52.6% → no se puede afirmar nada todavía.

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 14 | 57.1% |
| EUR/GBP | 9 | 77.8% |
| EUR/JPY | 8 | 62.5% |
| EUR/USD | 21 | 42.9% |
| GBP/JPY | 5 | 40.0% |
| GBP/USD | 18 | 72.2% |
| NZD/USD | 14 | 28.6% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 5 | 60.0% |
| USD/JPY | 3 | 33.3% |

