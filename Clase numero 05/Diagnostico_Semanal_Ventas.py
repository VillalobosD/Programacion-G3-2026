"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""
#datos originales
dias =["lunes", "martes", "miercoles", "jueves", "viernes"]
ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]

meta_centro = 640000
meta_norte = 700000
# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.
# TODO: calcula total, cantidad, mayor y menor para Centro.
#datos transformados
total_centro = sum(ventas_centro)#total de ventas semanal
cantidad_centro = len(ventas_centro)#cantidad de dias registrados
promedio_centro = total_centro / cantidad_centro#promedio de ventas diario
menor_centro = min(ventas_centro)#venta minima
mayor_centro = max(ventas_centro)#venta maxima
dia_mayor = dias[ventas_centro.index(mayor_centro)]
print(dia_mayor, mayor_centro)
porcentaje_centro = (total_centro * 100 )/ meta_centro 

# TODO: repite los indicadores para Norte.

total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
promedio_norte = total_norte / cantidad_norte
menor_norte = min(ventas_norte)
mayor_norte = max(ventas_norte)
porcentaje_norte = (total_norte * 100 )/ meta_norte

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro = "Meta superada"
elif total_centro == meta_centro:
    estado_centro = "meta alcanzada"
else:
    estado_centro = "a volar pala No alcanzo la META"
    
if total_norte > meta_norte:
    estado_norte = "Meta superada"
elif total_norte == meta_norte:
    estado_norte = "Meta alcanzada"
else:
    estado_norte = "a volar pala No alcanzo la META"
    

# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_mayor_ventas = "tienda del centro"
elif total_norte > total_centro:
    tienda_mayor_ventas = "tienda del norte"
else:
    tienda_mayor_ventas = "ambas tiendas se quedan "
    
# TODO: presenta un reporte con etiquetas claras y f-strings.

print('Comparacion semanal de tiendas')
print(f"Centro | total: ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento {porcentaje_centro:.0f}%")
print(f"Centro logro:  {estado_centro}")
print("-" * 50)
# TODO: escribe las tres conclusiones solicitadas en la guía.
print('Comparacion semanal de tiendas')
print(f"Norte | total: ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} | cumplimiento {porcentaje_norte:.0f}%")
print(f"Norte logro:  {estado_norte}")
print("-" * 50)

print("Tienda con mayor ventas :", tienda_mayor_ventas)
print("-" * 50)
