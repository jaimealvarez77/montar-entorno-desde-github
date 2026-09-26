"""
Ejemplo 2 · pandas: crear y resumir una tabla de ventas.
 
Genera 240 ventas de cuatro tiendas entre enero y junio de 2026 y responde a
tres preguntas de negocio con pandas. Los datos se crean con una semilla fija,
así que a todos los alumnos les salen los mismos resultados.
"""
import numpy as np
import pandas as pd
 
# ---- Crear los datos ----
generador = np.random.default_rng(2026)   # semilla fija: mismos datos siempre
n = 240
ventas = pd.DataFrame({
    "fecha": pd.to_datetime("2026-01-01") + pd.to_timedelta(generador.integers(0, 181, n), unit="D"),
    "tienda": generador.choice(["Madrid", "Barcelona", "Valencia", "Sevilla"], n, p=[0.32, 0.28, 0.21, 0.19]),
    "categoria": generador.choice(["Electrónica", "Hogar", "Moda", "Deportes"], n),
    "unidades": generador.integers(1, 7, n),
})
precio_base = ventas["categoria"].map({"Electrónica": 250, "Hogar": 60, "Moda": 50, "Deportes": 90})
ventas["precio_unitario"] = (precio_base * generador.uniform(0.5, 1.5, n)).round(2)
ventas = ventas.sort_values("fecha").reset_index(drop=True)
 
# Nueva columna calculada a partir de otras dos
ventas["importe"] = ventas["unidades"] * ventas["precio_unitario"]
 
print(f"La tabla tiene {len(ventas)} ventas y estas columnas: {list(ventas.columns)}")
print()
print("PRIMERAS FILAS")
print(ventas.head())
 
# Pregunta 1: ¿cuánto ha facturado cada tienda?
print()
print("FACTURACIÓN POR TIENDA (EUR)")
por_tienda = ventas.groupby("tienda")["importe"].sum().sort_values(ascending=False)
print(por_tienda.round(2))
 
# Pregunta 2: ¿qué categoría vende más en cada tienda?
print()
print("FACTURACIÓN POR TIENDA Y CATEGORÍA (EUR)")
tabla = ventas.pivot_table(index="tienda", columns="categoria", values="importe", aggfunc="sum")
print(tabla.round(0))
 
# Pregunta 3: ¿cómo evoluciona la facturación mes a mes?
print()
print("FACTURACIÓN MENSUAL (EUR)")
ventas["mes"] = ventas["fecha"].dt.month
por_mes = ventas.groupby("mes")["importe"].sum()
print(por_mes.round(2))