# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-11 12:45** (UTC) · 7 días con datos · 5.958 velas registradas · 246 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 31 | 48.4% | 32.0% a 65.2% | -8.1% | no se puede afirmar nada todavía |
| USD/CHF | 29 | 44.8% | 28.4% a 62.5% | -14.8% | muy pocos datos |
| GBP/USD | 28 | 35.7% | 20.7% a 54.2% | -32.1% | muy pocos datos |
| EUR/JPY | 25 | 52.0% | 33.5% a 70.0% | -1.2% | muy pocos datos |
| EUR/USD | 24 | 41.7% | 24.5% a 61.2% | -20.8% | muy pocos datos |
| EUR/GBP | 24 | 54.2% | 35.1% a 72.1% | +2.9% | muy pocos datos |
| NZD/USD | 23 | 43.5% | 25.6% a 63.2% | -17.4% | muy pocos datos |
| GBP/JPY | 23 | 52.2% | 33.0% a 70.8% | -0.9% | muy pocos datos |
| AUD/USD | 21 | 28.6% | 13.8% a 50.0% | -45.7% | muy pocos datos |
| USD/CAD | 18 | 50.0% | 29.0% a 71.0% | -5.0% | muy pocos datos |
| TODOS LOS PARES | 246 | 45.1% | 39.0% a 51.4% | -14.3% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 17 | 52.9% | 31.0% a 73.8% | +0.6% | muy pocos datos |
| USD/JPY | 16 | 43.8% | 23.1% a 66.8% | -16.9% | muy pocos datos |
| NZD/USD | 15 | 33.3% | 15.2% a 58.3% | -36.7% | muy pocos datos |
| USD/CHF | 14 | 42.9% | 21.4% a 67.4% | -18.6% | muy pocos datos |
| EUR/JPY | 11 | 54.5% | 28.0% a 78.7% | +3.6% | muy pocos datos |
| AUD/USD | 11 | 27.3% | 9.7% a 56.6% | -48.2% | muy pocos datos |
| USD/CAD | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| GBP/USD | 10 | 30.0% | 10.8% a 60.3% | -43.0% | muy pocos datos |
| GBP/JPY | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 116 | 42.2% | 33.6% a 51.3% | -19.7% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 15 | 46.7% | 24.8% a 69.9% | -11.3% | muy pocos datos |
| NZD/USD | 13 | 23.1% | 8.2% a 50.3% | -56.2% | muy pocos datos |
| USD/JPY | 13 | 46.2% | 23.2% a 70.9% | -12.3% | muy pocos datos |
| USD/CHF | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| EUR/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| USD/CAD | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| GBP/USD | 8 | 12.5% | 2.2% a 47.1% | -76.2% | muy pocos datos |
| AUD/USD | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| GBP/JPY | 6 | 16.7% | 3.0% a 56.4% | -68.3% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 96 | 37.5% | 28.5% a 47.5% | -28.7% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 70 | 42.9% |
| 06:00 a 13:00 | 03:00 a 10:00 | 77 | 58.4% |
| 13:00 a 21:00 | 10:00 a 18:00 | 92 | 33.7% |
| 21:00 a 24:00 | 18:00 a 21:00 | 7 | 71.4% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.0, EUR/GBP 3.4, EUR/JPY 3.6, EUR/USD 3.4, GBP/JPY 3.3, GBP/USD 4.0, NZD/USD 3.3, USD/CAD 2.6, USD/CHF 4.1, USD/JPY 4.4. **Total: 35.1 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 68 señales · acierto **48.5%** (rango 37.1% a 60.2%) · ganancia esperada -7.8% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

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
| USD/CHF | 2 | 100.0% |
| USD/JPY | 2 | 50.0% |

