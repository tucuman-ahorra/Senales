# Informe automático del escáner

Datos desde **2026-11-03 04:15** hasta **2026-11-10 10:00** (UTC) · 6 días con datos · 4.914 velas registradas · 204 señales.

Equilibrio con pago 90%: **52.6%**. Un resultado por debajo no gana plata; hace falta superarlo con margen.

Cómo leerlo: *Rango* es el margen razonable del acierto real dado el tamaño de la muestra. Como se miran muchos pares y niveles a la vez, algunos van a parecer buenos solo por azar; la marca **no es azar** aparece únicamente si sobrevive a la corrección de Holm.

## Normal o mejor (nivel ≥ 1)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| USD/JPY | 27 | 44.4% | 27.6% a 62.7% | -15.6% | muy pocos datos |
| USD/CHF | 25 | 44.0% | 26.7% a 62.9% | -16.4% | muy pocos datos |
| EUR/JPY | 22 | 50.0% | 30.7% a 69.3% | -5.0% | muy pocos datos |
| GBP/USD | 22 | 31.8% | 16.4% a 52.7% | -39.5% | muy pocos datos |
| NZD/USD | 20 | 40.0% | 21.9% a 61.3% | -24.0% | muy pocos datos |
| EUR/USD | 20 | 30.0% | 14.5% a 51.9% | -43.0% | muy pocos datos |
| GBP/JPY | 19 | 57.9% | 36.3% a 76.9% | +10.0% | muy pocos datos |
| EUR/GBP | 18 | 50.0% | 29.0% a 71.0% | -5.0% | muy pocos datos |
| AUD/USD | 16 | 25.0% | 10.2% a 49.5% | -52.5% | muy pocos datos |
| USD/CAD | 15 | 46.7% | 24.8% a 69.9% | -11.3% | muy pocos datos |
| TODOS LOS PARES | 204 | 42.2% | 35.6% a 49.0% | -19.9% | por debajo del equilibrio |

## Fuerte o mejor (nivel ≥ 2)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| NZD/USD | 13 | 30.8% | 12.7% a 57.6% | -41.5% | muy pocos datos |
| EUR/USD | 13 | 38.5% | 17.7% a 64.5% | -26.9% | muy pocos datos |
| USD/JPY | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| EUR/JPY | 10 | 50.0% | 23.7% a 76.3% | -5.0% | muy pocos datos |
| USD/CHF | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| USD/CAD | 9 | 33.3% | 12.1% a 64.6% | -36.7% | muy pocos datos |
| AUD/USD | 8 | 25.0% | 7.1% a 59.1% | -52.5% | muy pocos datos |
| GBP/USD | 7 | 14.3% | 2.6% a 51.3% | -72.9% | muy pocos datos |
| GBP/JPY | 4 | 50.0% | 15.0% a 85.0% | -5.0% | muy pocos datos |
| EUR/GBP | 3 | 100.0% | 43.8% a 100.0% | +90.0% | muy pocos datos |
| TODOS LOS PARES | 89 | 37.1% | 27.8% a 47.5% | -29.6% | por debajo del equilibrio |

## Muy fuerte (nivel 3)

| Par | Señales | Acierto | Rango | Ganancia esperada | Lectura |
|---|---|---|---|---|---|
| EUR/USD | 12 | 33.3% | 13.8% a 60.9% | -36.7% | muy pocos datos |
| NZD/USD | 11 | 18.2% | 5.1% a 47.7% | -65.5% | muy pocos datos |
| USD/JPY | 10 | 40.0% | 16.8% a 68.7% | -24.0% | muy pocos datos |
| EUR/JPY | 9 | 44.4% | 18.9% a 73.3% | -15.6% | muy pocos datos |
| USD/CHF | 9 | 33.3% | 12.1% a 64.6% | -36.7% | muy pocos datos |
| GBP/USD | 7 | 14.3% | 2.6% a 51.3% | -72.9% | muy pocos datos |
| USD/CAD | 7 | 42.9% | 15.8% a 75.0% | -18.6% | muy pocos datos |
| AUD/USD | 5 | 20.0% | 3.6% a 62.4% | -62.0% | muy pocos datos |
| EUR/GBP | 3 | 100.0% | 43.8% a 100.0% | +90.0% | muy pocos datos |
| GBP/JPY | 3 | 33.3% | 6.1% a 79.2% | -36.7% | muy pocos datos |
| TODOS LOS PARES | 76 | 34.2% | 24.5% a 45.4% | -35.0% | por debajo del equilibrio |

## Chequeo por franja horaria (todas las señales, todos los pares)

Si el acierto se concentra en una sola franja, sobre todo la de cierre diario (21 a 24 UTC = 18 a 21 hs en Tucumán), desconfiá: suele ser un artefacto de precios poco confiables.

| Franja (UTC) | Equivale en Tucumán | Señales | Acierto |
|---|---|---|---|
| 00:00 a 06:00 | 21:00 a 03:00 | 63 | 39.7% |
| 06:00 a 13:00 | 03:00 a 10:00 | 62 | 53.2% |
| 13:00 a 21:00 | 10:00 a 18:00 | 72 | 31.9% |
| 21:00 a 24:00 | 18:00 a 21:00 | 7 | 71.4% |

## Cuántas señales entran por día

Promedio de señales por día (todos los niveles): AUD/USD 2.7, EUR/GBP 3.0, EUR/JPY 3.7, EUR/USD 3.3, GBP/JPY 3.2, GBP/USD 3.7, NZD/USD 3.3, USD/CAD 2.5, USD/CHF 4.2, USD/JPY 4.5. **Total: 34.0 por día.**

> Los números de esta página son resultados *teóricos* (entrada al abrir la vela siguiente, vencimiento al cerrarla, empate = pérdida). No incluyen spread, retrasos ni diferencias de precio de tu plataforma. Ningún resultado de acá es garantía de ganancia.
## Modelo de 30 minutos (en vivo)

Cada señal que el modelo marcó en datos recientes (todos posteriores a 2025, que el modelo nunca vio al entrenar), con su resultado teórico. **Esta es la prueba real.**

**Total:** 57 señales · acierto **45.6%** (rango 33.4% a 58.4%) · ganancia esperada -13.3% por operación · equilibrio 52.6% → muy pocas señales: todavía no se puede afirmar nada (hacen falta 300 o más).

| Par | Señales | Acierto |
|---|---|---|
| AUD/USD | 8 | 50.0% |
| EUR/GBP | 6 | 83.3% |
| EUR/JPY | 1 | 100.0% |
| EUR/USD | 14 | 35.7% |
| GBP/USD | 10 | 50.0% |
| NZD/USD | 11 | 27.3% |
| USD/CAD | 3 | 0.0% |
| USD/CHF | 2 | 100.0% |
| USD/JPY | 2 | 50.0% |

