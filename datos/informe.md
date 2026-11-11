# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-11 21:15** (UTC) · 7 días con datos · 6.298 velas registradas · 261 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 31 | 48.4% | 32.0% a 65.2% | -8.1% | no se puede afirmar nada todavía |
| GBP/USD | 31 | 32.3% | 18.6% a 49.9% | -38.7% | por debajo del equilibrio |
| USD/CHF | 31 | 41.9% | 26.4% a 59.2% | -20.3% | no se puede afirmar nada todavía |
| EUR/USD | 29 | 37.9% | 22.7% a 56.0% | -27.9% | muy pocos datos |
| GBP/JPY | 26 | 46.2% | 28.8% a 64.5% | -12.3% | muy pocos datos |
| EUR/JPY | 26 | 50.0% | 32.1% a 67.9% | -5.0% | muy pocos datos |
| NZD/USD | 24 | 45.8% | 27.9% a 64.9% | -12.9% | muy pocos datos |
| EUR/GBP | 24 | 54.2% | 35.1% a 72.1% | +2.9% | muy pocos datos |
| AUD/USD | 21 | 28.6% | 13.8% a 50.0% | -45.7% | muy pocos datos |
| USD/CAD | 18 | 50.0% | 29.0% a 71.0% | -5.0% | muy pocos datos |
| TODOS LOS PARES | 261 | 43.3% | 37.4% a 49.4% | -17.7% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 22 | 45.5% | 26.9% a 65.3% | -13.6% | muy pocos datos |
| USD/JPY | 16 | 43.8% | 23.1% a 66.8% | -16.9% | muy pocos datos |
| USD/CHF | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| NZD/USD | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| GBP/USD | 13 | 23.1% | 8.2% a 50.3% | -56.2% | muy pocos datos |
| AUD/USD | 11 | 27.3% | 9.7% a 56.6% | -48.2% | muy pocos datos |
| USD/CAD | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| EUR/JPY | 11 | 54.5% | 28.0% a 78.7% | +3.6% | muy pocos datos |
| GBP/JPY | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 127 | 40.2% | 32.0% a 48.9% | -23.7% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 20 | 40.0% | 21.9% a 61.3% | -24.0% | muy pocos datos |
| NZD/USD | 14 | 28.6% | 11.7% a 54.6% | -45.7% | muy pocos datos |
| USD/CHF | 14 | 28.6% | 11.7% a 54.6% | -45.7% | muy pocos datos |
| USD/JPY | 13 | 46.2% | 23.2% a 70.9% | -12.3% | muy pocos datos |
| GBP/USD | 11 | 9.1% | 1.6% a 37.7% | -82.7% | muy pocos datos |
| EUR/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| USD/CAD | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| AUD/USD | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| GBP/JPY | 6 | 16.7% | 3.0% a 56.4% | -68.3% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 107 | 35.5% | 27.1% a 44.9% | -32.5% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 70 | 42.9% |
| 06:00 a 13:00 | 03:00 a 10:00 | 77 | 58.4% |
| 13:00 a 21:00 | 10:00 a 18:00 | 106 | 31.1% |
| 21:00 a 24:00 | 18:00 a 21:00 | 8 | 62.5% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.0, EUR/GBP 3.4, EUR/JPY 3.7, EUR/USD 4.1, GBP/JPY 3.7, GBP/USD 4.4, NZD/USD 3.4, USD/CAD 2.6, USD/CHF 4.4, USD/JPY 4.4. **Total: 37.3 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 69 señales · acierto **47.8%** (rango 36.5% a 59.4%) · ganancia esperada -9.1% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 9 | 44.4% |
| EUR/GBP | 8 | 75.0% |
| EUR/JPY | 2 | 100.0% |
| EUR/USD | 15 | 40.0% |
| GBP/JPY | 1 | 0.0% |
| GBP/USD | 13 | 61.5% |
| NZD/USD | 13 | 30.8% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 3 | 66.7% |
| USD/JPY | 2 | 50.0% |

