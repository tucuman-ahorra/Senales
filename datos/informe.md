# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-19 21:45** (UTC) · 13 días con datos · 11.847 velas registradas · 474 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| GBP/JPY | 52 | 51.9% | 38.7% a 64.9% | -1.3% | no se puede afirmar nada todavía |
| AUD/USD | 51 | 31.4% | 20.3% a 45.0% | -40.4% | por debajo del equilibrio |
| GBP/USD | 51 | 45.1% | 32.3% a 58.6% | -14.3% | no se puede afirmar nada todavía |
| EUR/JPY | 51 | 45.1% | 32.3% a 58.6% | -14.3% | no se puede afirmar nada todavía |
| USD/JPY | 50 | 56.0% | 42.3% a 68.8% | +6.4% | no se puede afirmar nada todavía |
| USD/CHF | 47 | 51.1% | 37.2% a 64.7% | -3.0% | no se puede afirmar nada todavía |
| NZD/USD | 46 | 45.7% | 32.2% a 59.8% | -13.3% | no se puede afirmar nada todavía |
| EUR/GBP | 45 | 57.8% | 43.3% a 71.0% | +9.8% | no se puede afirmar nada todavía |
| EUR/USD | 45 | 42.2% | 29.0% a 56.7% | -19.8% | no se puede afirmar nada todavía |
| USD/CAD | 36 | 58.3% | 42.2% a 72.9% | +10.8% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 474 | 48.1% | 43.6% a 52.6% | -8.6% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 24 | 50.0% | 31.4% a 68.6% | -5.0% | muy pocos datos |
| AUD/USD | 23 | 39.1% | 22.2% a 59.2% | -25.7% | muy pocos datos |
| NZD/USD | 22 | 36.4% | 19.7% a 57.0% | -30.9% | muy pocos datos |
| USD/JPY | 21 | 57.1% | 36.5% a 75.5% | +8.6% | muy pocos datos |
| GBP/USD | 21 | 38.1% | 20.8% a 59.1% | -27.6% | muy pocos datos |
| EUR/JPY | 20 | 50.0% | 29.9% a 70.1% | -5.0% | muy pocos datos |
| USD/CHF | 19 | 47.4% | 27.3% a 68.3% | -10.0% | muy pocos datos |
| GBP/JPY | 13 | 53.8% | 29.1% a 76.8% | +2.3% | muy pocos datos |
| USD/CAD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| EUR/GBP | 9 | 55.6% | 26.7% a 81.1% | +5.6% | muy pocos datos |
| TODOS LOS PARES | 184 | 45.7% | 38.6% a 52.9% | -13.3% | no se puede afirmar nada todavía |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 22 | 45.5% | 26.9% a 65.3% | -13.6% | muy pocos datos |
| GBP/USD | 19 | 31.6% | 15.4% a 54.0% | -40.0% | muy pocos datos |
| USD/JPY | 18 | 61.1% | 38.6% a 79.7% | +16.1% | muy pocos datos |
| NZD/USD | 18 | 33.3% | 16.3% a 56.3% | -36.7% | muy pocos datos |
| USD/CHF | 17 | 41.2% | 21.6% a 64.0% | -21.8% | muy pocos datos |
| AUD/USD | 17 | 47.1% | 26.2% a 69.0% | -10.6% | muy pocos datos |
| EUR/JPY | 17 | 41.2% | 21.6% a 64.0% | -21.8% | muy pocos datos |
| USD/CAD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| EUR/GBP | 9 | 55.6% | 26.7% a 81.1% | +5.6% | muy pocos datos |
| GBP/JPY | 8 | 37.5% | 13.7% a 69.4% | -28.7% | muy pocos datos |
| TODOS LOS PARES | 155 | 43.2% | 35.7% a 51.1% | -17.9% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 122 | 49.2% |
| 06:00 a 13:00 | 03:00 a 10:00 | 125 | 60.8% |
| 13:00 a 21:00 | 10:00 a 18:00 | 189 | 37.0% |
| 21:00 a 24:00 | 18:00 a 21:00 | 38 | 57.9% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.9, EUR/GBP 3.5, EUR/JPY 3.9, EUR/USD 3.5, GBP/JPY 4.0, GBP/USD 3.9, NZD/USD 3.5, USD/CAD 2.8, USD/CHF 3.6, USD/JPY 3.8. **Total: 36.5 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 111 señales · acierto **50.5%** (rango 41.3% a 59.6%) · ganancia esperada -4.1% por operación · equilibrio 52.6% → no se puede afirmar nada todavía.

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 16 | 56.2% |
| EUR/GBP | 14 | 57.1% |
| EUR/JPY | 8 | 62.5% |
| EUR/USD | 23 | 39.1% |
| GBP/JPY | 5 | 40.0% |
| GBP/USD | 19 | 73.7% |
| NZD/USD | 14 | 28.6% |
| USD/CAD | 4 | 25.0% |
| USD/CHF | 5 | 60.0% |
| USD/JPY | 3 | 33.3% |

