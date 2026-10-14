#entradas
producto = ["Cafe", 5000, 20]
aumento = 10
descuento = producto[1] * 15 / 100
precio_promocional = producto[1] - descuento

ingreso_actual = producto[1] * producto[2]
#proceso
proyeccion = producto[2] * 10 / 100

unidades_proyectas = producto[2] + proyeccion

ventas_proyectadas = precio_promocional * unidades_proyectas

ingreso_promocional = ventas_proyectadas - ingreso_actual

#print(descuento)
#print(precio_promocional)
#print(ingreso_actual)
#print(proyeccion)
#print(ventas_proyectadas)
#print(ingreso_promocional)

if ingreso_promocional > 0:
    recomendacion = 'lanzar'
else:
    recomendacion = 'No lanzar la promo'

print('ANÁLISIS DE PROMOCIÓN')
print(f"Producto:{producto[0]:}" )
print(f"Precio actual:{producto[1]:}" )
print(f"Cantidades actuales:₡{producto[2]:}" )
print(f"Ingreso Actual:₡{ingreso_actual:.0f}" )
print(f"Descuento por Unidad:₡{descuento:.0f}" )
print(f"Precio Promocional:₡{precio_promocional:.0f}")
print(f"Aumento esperado: {aumento:.0f}%")
print(f"Unidades Proyectadas:{unidades_proyectas:.0f}" )
print(f"Ingreso por Promocion:₡{ventas_proyectadas:.0f}" )
print(f"Diferencia:₡{ingreso_promocional:.0f}")
print('La recomencacion es:',recomendacion)



