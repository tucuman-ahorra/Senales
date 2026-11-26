# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-26 17:15** (UTC) · 18 días con datos · 16.223 velas registradas · 598 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 67 | 55.2% | 43.4% a 66.5% | +4.9% | no se puede afirmar nada todavía |
| EUR/GBP | 65 | 58.5% | 46.3% a 69.6% | +11.1% | no se puede afirmar nada todavía |
| GBP/JPY | 65 | 55.4% | 43.3% a 66.8% | +5.2% | no se puede afirmar nada todavía |
| EUR/JPY | 64 | 50.0% | 38.1% a 61.9% | -5.0% | no se puede afirmar nada todavía |
| GBP/USD | 63 | 46.0% | 34.3% a 58.2% | -12.5% | no se puede afirmar nada todavía |
| AUD/USD | 62 | 35.5% | 24.7% a 47.9% | -32.6% | por debajo del equilibrio |
| EUR/USD | 57 | 38.6% | 27.1% a 51.6% | -26.7% | por debajo del equilibrio |
| USD/CHF | 57 | 56.1% | 43.3% a 68.2% | +6.7% | no se puede afirmar nada todavía |
| NZD/USD | 53 | 47.2% | 34.4% a 60.3% | -10.4% | no se puede afirmar nada todavía |
| USD/CAD | 45 | 55.6% | 41.2% a 69.1% | +5.6% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 598 | 49.8% | 45.8% a 53.8% | -5.3% | no se puede afirmar nada todavía |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 28 | 42.9% | 26.5% a 60.9% | -18.6% | muy pocos datos |
| AUD/USD | 26 | 38.5% | 22.4% a 57.5% | -26.9% | muy pocos datos |
| USD/JPY | 25 | 60.0% | 40.7% a 76.6% | +14.0% | muy pocos datos |
| NZD/USD | 24 | 37.5% | 21.2% a 57.3% | -28.7% | muy pocos datos |
| EUR/JPY | 24 | 58.3% | 38.8% a 75.5% | +10.8% | muy pocos datos |
| USD/CHF | 23 | 52.2% | 33.0% a 70.8% | -0.9% | muy pocos datos |
| GBP/USD | 22 | 36.4% | 19.7% a 57.0% | -30.9% | muy pocos datos |
| GBP/JPY | 21 | 61.9% | 40.9% a 79.2% | +17.6% | muy pocos datos |
| EUR/GBP | 14 | 57.1% | 32.6% a 78.6% | +8.6% | muy pocos datos |
| USD/CAD | 14 | 35.7% | 16.3% a 61.2% | -32.1% | muy pocos datos |
| TODOS LOS PARES | 221 | 48.0% | 41.5% a 54.5% | -8.9% | no se puede afirmar nada todavía |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 26 | 38.5% | 22.4% a 57.5% | -26.9% | muy pocos datos |
| USD/JPY | 22 | 63.6% | 43.0% a 80.3% | +20.9% | muy pocos datos |
| USD/CHF | 21 | 47.6% | 28.3% a 67.6% | -9.5% | muy pocos datos |
| EUR/JPY | 21 | 52.4% | 32.4% a 71.7% | -0.5% | muy pocos datos |
| NZD/USD | 20 | 35.0% | 18.1% a 56.7% | -33.5% | muy pocos datos |
| GBP/USD | 19 | 31.6% | 15.4% a 54.0% | -40.0% | muy pocos datos |
| AUD/USD | 18 | 50.0% | 29.0% a 71.0% | -5.0% | muy pocos datos |
| GBP/JPY | 16 | 56.2% | 33.2% a 76.9% | +6.9% | muy pocos datos |
| EUR/GBP | 13 | 53.8% | 29.1% a 76.8% | +2.3% | muy pocos datos |
| USD/CAD | 12 | 41.7% | 19.3% a 68.0% | -20.8% | muy pocos datos |
| TODOS LOS PARES | 188 | 46.8% | 39.8% a 53.9% | -11.1% | no se puede afirmar nada todavía |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 152 | 51.3% |
| 06:00 a 13:00 | 03:00 a 10:00 | 172 | 61.0% |
| 13:00 a 21:00 | 10:00 a 18:00 | 229 | 37.6% |
| 21:00 a 24:00 | 18:00 a 21:00 | 45 | 64.4% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.4, EUR/GBP 3.6, EUR/JPY 3.6, EUR/USD 3.2, GBP/JPY 3.6, GBP/USD 3.5, NZD/USD 2.9, USD/CAD 2.5, USD/CHF 3.2, USD/JPY 3.7. **Total: 33.2 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 157 señales · acierto **49.7%** (rango 42.0% a 57.4%) · ganancia esperada -5.6% por operación · equilibrio 52.6% → no se puede afirmar nada todavía.

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 25 | 60.0% |
| EUR/GBP | 18 | 55.6% |
| EUR/JPY | 13 | 53.8% |
| EUR/USD | 33 | 36.4% |
| GBP/JPY | 6 | 33.3% |
| GBP/USD | 25 | 68.0% |
| NZD/USD | 21 | 28.6% |
| USD/CAD | 5 | 40.0% |
| USD/CHF | 6 | 66.7% |
| USD/JPY | 5 | 60.0% |

