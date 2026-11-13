# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-13 08:45** (UTC) · 9 días con datos · 7.651 velas registradas · 345 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| GBP/JPY | 40 | 50.0% | 35.2% a 64.8% | -5.0% | no se puede afirmar nada todavía |
| GBP/USD | 39 | 33.3% | 20.6% a 49.0% | -36.7% | por debajo del equilibrio |
| USD/JPY | 39 | 51.3% | 36.2% a 66.1% | -2.6% | no se puede afirmar nada todavía |
| USD/CHF | 38 | 47.4% | 32.5% a 62.7% | -10.0% | no se puede afirmar nada todavía |
| EUR/JPY | 36 | 50.0% | 34.5% a 65.5% | -5.0% | no se puede afirmar nada todavía |
| EUR/USD | 36 | 38.9% | 24.8% a 55.1% | -26.1% | no se puede afirmar nada todavía |
| AUD/USD | 32 | 25.0% | 13.3% a 42.1% | -52.5% | por debajo del equilibrio |
| EUR/GBP | 29 | 55.2% | 37.5% a 71.6% | +4.8% | muy pocos datos |
| NZD/USD | 29 | 48.3% | 31.4% a 65.6% | -8.3% | muy pocos datos |
| USD/CAD | 27 | 55.6% | 37.3% a 72.4% | +5.6% | muy pocos datos |
| TODOS LOS PARES | 345 | 45.2% | 40.0% a 50.5% | -14.1% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 23 | 47.8% | 29.2% a 67.0% | -9.1% | muy pocos datos |
| NZD/USD | 18 | 38.9% | 20.3% a 61.4% | -26.1% | muy pocos datos |
| USD/JPY | 17 | 47.1% | 26.2% a 69.0% | -10.6% | muy pocos datos |
| GBP/USD | 17 | 23.5% | 9.6% a 47.3% | -55.3% | muy pocos datos |
| USD/CHF | 16 | 37.5% | 18.5% a 61.4% | -28.7% | muy pocos datos |
| AUD/USD | 15 | 33.3% | 15.2% a 58.3% | -36.7% | muy pocos datos |
| USD/CAD | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| EUR/JPY | 11 | 54.5% | 28.0% a 78.7% | +3.6% | muy pocos datos |
| GBP/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 141 | 41.8% | 34.0% a 50.1% | -20.5% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 21 | 42.9% | 24.5% a 63.5% | -18.6% | muy pocos datos |
| GBP/USD | 15 | 13.3% | 3.7% a 37.9% | -74.7% | muy pocos datos |
| NZD/USD | 15 | 33.3% | 15.2% a 58.3% | -36.7% | muy pocos datos |
| USD/CHF | 14 | 28.6% | 11.7% a 54.6% | -45.7% | muy pocos datos |
| USD/JPY | 14 | 50.0% | 26.8% a 73.2% | -5.0% | muy pocos datos |
| AUD/USD | 11 | 36.4% | 15.2% a 64.6% | -30.9% | muy pocos datos |
| USD/CAD | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| EUR/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| GBP/JPY | 6 | 16.7% | 3.0% a 56.4% | -68.3% | muy pocos datos |
| EUR/GBP | 4 | 100.0% | 51.0% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 118 | 37.3% | 29.1% a 46.3% | -29.2% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 95 | 44.2% |
| 06:00 a 13:00 | 03:00 a 10:00 | 90 | 58.9% |
| 13:00 a 21:00 | 10:00 a 18:00 | 132 | 34.1% |
| 21:00 a 24:00 | 18:00 a 21:00 | 28 | 57.1% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 3.6, EUR/GBP 3.2, EUR/JPY 4.0, EUR/USD 4.0, GBP/JPY 4.4, GBP/USD 4.3, NZD/USD 3.2, USD/CAD 3.0, USD/CHF 4.2, USD/JPY 4.3. **Total: 38.3 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 74 señales · acierto **48.6%** (rango 37.6% a 59.8%) · ganancia esperada -7.6% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 10 | 50.0% |
| EUR/GBP | 9 | 77.8% |
| EUR/JPY | 2 | 100.0% |
| EUR/USD | 16 | 37.5% |
| GBP/JPY | 1 | 0.0% |
| GBP/USD | 14 | 64.3% |
| NZD/USD | 13 | 30.8% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 4 | 50.0% |
| USD/JPY | 2 | 50.0% |

