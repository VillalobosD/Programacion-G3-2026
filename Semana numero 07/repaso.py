from sedes import empredimientos

print("Emprendimientos registrados:", len(empredimientos))
print("Primer emprendimiento:", empredimientos[-1]["nombre"])
print("Primer emprendimiento ventas:", empredimientos[-1]["ventas"])

print("\nANALISIS SEMANAL DE EMPRENDEDORES")
provincias = set() # provincias = {1,2,3,4}

#Cada vuelta procesara un diccionario
for e in empredimientos:
    print (e)