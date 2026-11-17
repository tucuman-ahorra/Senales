# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-17 08:15** (UTC) · 11 días con datos · 9.438 velas registradas · 394 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 45 | 53.3% | 39.1% a 67.1% | +1.3% | no se puede afirmar nada todavía |
| GBP/USD | 43 | 39.5% | 26.4% a 54.4% | -24.9% | no se puede afirmar nada todavía |
| GBP/JPY | 42 | 52.4% | 37.7% a 66.6% | -0.5% | no se puede afirmar nada todavía |
| EUR/JPY | 42 | 47.6% | 33.4% a 62.3% | -9.5% | no se puede afirmar nada todavía |
| EUR/USD | 41 | 39.0% | 25.7% a 54.3% | -25.9% | no se puede afirmar nada todavía |
| USD/CHF | 41 | 46.3% | 32.1% a 61.3% | -12.0% | no se puede afirmar nada todavía |
| AUD/USD | 38 | 31.6% | 19.1% a 47.5% | -40.0% | por debajo del equilibrio |
| EUR/GBP | 36 | 52.8% | 37.0% a 68.0% | +0.3% | no se puede afirmar nada todavía |
| NZD/USD | 34 | 50.0% | 34.1% a 65.9% | -5.0% | no se puede afirmar nada todavía |
| USD/CAD | 32 | 56.2% | 39.3% a 71.8% | +6.9% | no se puede afirmar nada todavía |
| TODOS LOS PARES | 394 | 46.7% | 41.8% a 51.6% | -11.3% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 23 | 47.8% | 29.2% a 67.0% | -9.1% | muy pocos datos |
| AUD/USD | 19 | 36.8% | 19.1% a 59.0% | -30.0% | muy pocos datos |
| NZD/USD | 19 | 42.1% | 23.1% a 63.7% | -20.0% | muy pocos datos |
| USD/JPY | 18 | 50.0% | 29.0% a 71.0% | -5.0% | muy pocos datos |
| GBP/USD | 17 | 23.5% | 9.6% a 47.3% | -55.3% | muy pocos datos |
| USD/CHF | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| EUR/JPY | 14 | 50.0% | 26.8% a 73.2% | -5.0% | muy pocos datos |
| USD/CAD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| GBP/JPY | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| EUR/GBP | 7 | 57.1% | 25.0% a 84.2% | +8.6% | muy pocos datos |
| TODOS LOS PARES | 155 | 41.9% | 34.5% a 49.8% | -20.3% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 21 | 42.9% | 24.5% a 63.5% | -18.6% | muy pocos datos |
| NZD/USD | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| USD/JPY | 15 | 53.3% | 30.1% a 75.2% | +1.3% | muy pocos datos |
| AUD/USD | 15 | 40.0% | 19.8% a 64.3% | -24.0% | muy pocos datos |
| GBP/USD | 15 | 13.3% | 3.7% a 37.9% | -74.7% | muy pocos datos |
| USD/CHF | 14 | 28.6% | 11.7% a 54.6% | -45.7% | muy pocos datos |
| EUR/JPY | 12 | 41.7% | 19.3% a 68.0% | -20.8% | muy pocos datos |
| USD/CAD | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| EUR/GBP | 7 | 57.1% | 25.0% a 84.2% | +8.6% | muy pocos datos |
| GBP/JPY | 7 | 28.6% | 8.2% a 64.1% | -45.7% | muy pocos datos |
| TODOS LOS PARES | 132 | 37.9% | 30.1% a 46.4% | -28.0% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 109 | 46.8% |
| 06:00 a 13:00 | 03:00 a 10:00 | 97 | 61.9% |
| 13:00 a 21:00 | 10:00 a 18:00 | 157 | 36.3% |
| 21:00 a 24:00 | 18:00 a 21:00 | 31 | 51.6% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.5, EUR/GBP 3.3, EUR/JPY 3.8, EUR/USD 3.7, GBP/JPY 3.8, GBP/USD 3.9, NZD/USD 3.1, USD/CAD 2.9, USD/CHF 3.7, USD/JPY 4.1. **Total: 35.8 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 87 señales · acierto **50.6%** (rango 40.3% a 60.8%) · ganancia esperada -3.9% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 12 | 58.3% |
| EUR/GBP | 9 | 77.8% |
| EUR/JPY | 4 | 75.0% |
| EUR/USD | 20 | 40.0% |
| GBP/JPY | 3 | 33.3% |
| GBP/USD | 15 | 66.7% |
| NZD/USD | 13 | 30.8% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 5 | 60.0% |
| USD/JPY | 3 | 33.3% |

