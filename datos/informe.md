# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-12 15:45** (UTC) · 8 días con datos · 7.004 velas registradas · 323 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| GBP/USD | 39 | 33.3% | 20.6% a 49.0% | -36.7% | por debajo del equilibrio |
| USD/JPY | 38 | 50.0% | 34.8% a 65.2% | -5.0% | no se puede afirmar nada todavía |
| GBP/JPY | 36 | 47.2% | 32.0% a 63.0% | -10.3% | no se puede afirmar nada todavía |
| USD/CHF | 35 | 45.7% | 30.5% a 61.8% | -13.1% | no se puede afirmar nada todavía |
| EUR/USD | 34 | 38.2% | 23.9% a 55.0% | -27.4% | no se puede afirmar nada todavía |
| EUR/JPY | 33 | 48.5% | 32.5% a 64.8% | -7.9% | no se puede afirmar nada todavía |
| AUD/USD | 29 | 27.6% | 14.7% a 45.7% | -47.6% | muy pocos datos |
| NZD/USD | 28 | 46.4% | 29.5% a 64.2% | -11.8% | muy pocos datos |
| USD/CAD | 26 | 53.8% | 35.5% a 71.2% | +2.3% | muy pocos datos |
| EUR/GBP | 25 | 56.0% | 37.1% a 73.3% | +6.4% | muy pocos datos |
| TODOS LOS PARES | 323 | 44.3% | 39.0% a 49.7% | -15.9% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 23 | 47.8% | 29.2% a 67.0% | -9.1% | muy pocos datos |
| NZD/USD | 18 | 38.9% | 20.3% a 61.4% | -26.1% | muy pocos datos |
| GBP/USD | 17 | 23.5% | 9.6% a 47.3% | -55.3% | muy pocos datos |
| USD/CHF | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| USD/JPY | 16 | 43.8% | 23.1% a 66.8% | -16.9% | muy pocos datos |
| AUD/USD | 15 | 33.3% | 15.2% a 58.3% | -36.7% | muy pocos datos |
| USD/CAD | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| EUR/JPY | 11 | 54.5% | 28.0% a 78.7% | +3.6% | muy pocos datos |
| GBP/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 140 | 41.4% | 33.6% a 49.7% | -21.3% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 21 | 42.9% | 24.5% a 63.5% | -18.6% | muy pocos datos |
| GBP/USD | 15 | 13.3% | 3.7% a 37.9% | -74.7% | muy pocos datos |
| NZD/USD | 15 | 33.3% | 15.2% a 58.3% | -36.7% | muy pocos datos |
| USD/CHF | 14 | 28.6% | 11.7% a 54.6% | -45.7% | muy pocos datos |
| USD/JPY | 13 | 46.2% | 23.2% a 70.9% | -12.3% | muy pocos datos |
| AUD/USD | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| USD/CAD | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| EUR/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| GBP/JPY | 6 | 16.7% | 3.0% a 56.4% | -68.3% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 117 | 36.8% | 28.6% a 45.8% | -30.2% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 89 | 44.9% |
| 06:00 a 13:00 | 03:00 a 10:00 | 83 | 56.6% |
| 13:00 a 21:00 | 10:00 a 18:00 | 127 | 33.9% |
| 21:00 a 24:00 | 18:00 a 21:00 | 24 | 54.2% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.6, EUR/GBP 3.1, EUR/JPY 4.1, EUR/USD 4.2, GBP/JPY 4.5, GBP/USD 4.9, NZD/USD 3.5, USD/CAD 3.2, USD/CHF 4.4, USD/JPY 4.8. **Total: 40.4 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 72 señales · acierto **47.2%** (rango 36.1% a 58.6%) · ganancia esperada -10.3% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

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
| USD/CHF | 4 | 50.0% |
| USD/JPY | 2 | 50.0% |

