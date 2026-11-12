# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-12 14:45** (UTC) · 8 días con datos · 6.964 velas registradas · 309 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 36 | 52.8% | 37.0% a 68.0% | +0.3% | no se puede afirmar nada todavía |
| GBP/USD | 36 | 33.3% | 20.2% a 49.7% | -36.7% | por debajo del equilibrio |
| USD/CHF | 35 | 45.7% | 30.5% a 61.8% | -13.1% | no se puede afirmar nada todavía |
| GBP/JPY | 34 | 47.1% | 31.5% a 63.3% | -10.6% | no se puede afirmar nada todavía |
| EUR/USD | 33 | 39.4% | 24.7% a 56.3% | -25.2% | no se puede afirmar nada todavía |
| EUR/JPY | 32 | 46.9% | 30.9% a 63.6% | -10.9% | no se puede afirmar nada todavía |
| NZD/USD | 27 | 48.1% | 30.7% a 66.0% | -8.5% | muy pocos datos |
| AUD/USD | 26 | 30.8% | 16.5% a 50.0% | -41.5% | muy pocos datos |
| EUR/GBP | 25 | 56.0% | 37.1% a 73.3% | +6.4% | muy pocos datos |
| USD/CAD | 25 | 52.0% | 33.5% a 70.0% | -1.2% | muy pocos datos |
| TODOS LOS PARES | 309 | 45.0% | 39.5% a 50.6% | -14.5% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 23 | 47.8% | 29.2% a 67.0% | -9.1% | muy pocos datos |
| NZD/USD | 18 | 38.9% | 20.3% a 61.4% | -26.1% | muy pocos datos |
| USD/CHF | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| USD/JPY | 16 | 43.8% | 23.1% a 66.8% | -16.9% | muy pocos datos |
| GBP/USD | 15 | 20.0% | 7.0% a 45.2% | -62.0% | muy pocos datos |
| AUD/USD | 14 | 35.7% | 16.3% a 61.2% | -32.1% | muy pocos datos |
| USD/CAD | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| EUR/JPY | 11 | 54.5% | 28.0% a 78.7% | +3.6% | muy pocos datos |
| GBP/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 137 | 41.6% | 33.7% a 50.0% | -20.9% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 21 | 42.9% | 24.5% a 63.5% | -18.6% | muy pocos datos |
| NZD/USD | 15 | 33.3% | 15.2% a 58.3% | -36.7% | muy pocos datos |
| USD/CHF | 14 | 28.6% | 11.7% a 54.6% | -45.7% | muy pocos datos |
| GBP/USD | 13 | 7.7% | 1.4% a 33.3% | -85.4% | muy pocos datos |
| USD/JPY | 13 | 46.2% | 23.2% a 70.9% | -12.3% | muy pocos datos |
| AUD/USD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| USD/CAD | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| EUR/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| GBP/JPY | 6 | 16.7% | 3.0% a 56.4% | -68.3% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 114 | 36.8% | 28.6% a 46.0% | -30.0% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 89 | 44.9% |
| 06:00 a 13:00 | 03:00 a 10:00 | 83 | 56.6% |
| 13:00 a 21:00 | 10:00 a 18:00 | 113 | 34.5% |
| 21:00 a 24:00 | 18:00 a 21:00 | 24 | 54.2% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.2, EUR/GBP 3.1, EUR/JPY 4.0, EUR/USD 4.1, GBP/JPY 4.2, GBP/USD 4.5, NZD/USD 3.4, USD/CAD 3.1, USD/CHF 4.4, USD/JPY 4.5. **Total: 38.6 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 71 señales · acierto **47.9%** (rango 36.7% a 59.3%) · ganancia esperada -9.0% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 9 | 44.4% |
| EUR/GBP | 8 | 75.0% |
| EUR/JPY | 2 | 100.0% |
| EUR/USD | 16 | 37.5% |
| GBP/JPY | 1 | 0.0% |
| GBP/USD | 14 | 64.3% |
| NZD/USD | 13 | 30.8% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 3 | 66.7% |
| USD/JPY | 2 | 50.0% |

