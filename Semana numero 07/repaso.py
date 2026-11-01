from sedes import empredimientos

print("Emprendimientos registrados:", len(empredimientos))
print("Primer emprendimiento:", empredimientos[0]["nombre"])
print("Primer emprendimiento ventas:", empredimientos[0]["ventas"])

print("\nANALISIS SEMANAL DE EMPRENDEDORES")
provincias = set() # provincias = {1,2,3,4}

#Cada vuelta procesara un diccionario
for e in empredimientos:
    total = sum(e["ventas"])
    porcentaje = (total / e["meta"]) * 100
    if porcentaje >= 100:
        estado = "Cumplio la meta"
    elif porcentaje >= 80:
        estado = "por poco y cerramos"
    else:
        estado = "critico"
    print(
        f"{e['nombre']}: ${total:,.2f} ({porcentaje:,.2f}%)- {estado}"
    )