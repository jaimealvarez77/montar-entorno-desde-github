"""
Ejemplo 1 · NumPy: cálculos con vectores de números.
 
Una tienda vende cinco productos. Con NumPy se calculan de una vez los importes,
los totales y el efecto de un descuento, sin escribir ningún bucle.
"""
import numpy as np
 
# Datos de partida: precio y unidades vendidas de cada producto
productos = ["portátil", "ratón", "teclado", "monitor", "auriculares"]
precios = np.array([749.0, 19.9, 45.5, 189.0, 59.9])
unidades = np.array([12, 85, 40, 18, 33])
 
# Operaciones elemento a elemento: cada precio por sus unidades
importes = precios * unidades
 
print("IMPORTE POR PRODUCTO")
for producto, importe in zip(productos, importes):
    print(f"  {producto:<12} {importe:>10.2f} EUR")
 
# Estadísticos básicos sobre el vector de importes
print()
print(f"Total vendido:        {importes.sum():>10.2f} EUR")
print(f"Importe medio:        {importes.mean():>10.2f} EUR")
print(f"Desviación típica:    {importes.std():>10.2f} EUR")
print(f"Producto que más factura: {productos[importes.argmax()]}")
 
# Un descuento del 10 % solo a los productos de más de 100 euros
precios_rebajados = np.where(precios > 100, precios * 0.90, precios)
ahorro = (precios - precios_rebajados) * unidades
print(f"Con un 10 % de descuento en lo que pasa de 100 EUR, los clientes ahorrarían {ahorro.sum():.2f} EUR")