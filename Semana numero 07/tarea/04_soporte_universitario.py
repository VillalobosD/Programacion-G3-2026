"""Caso 4: analice los registros de soporte sin crear funciones propias."""
             
# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).


from incidencias import incidencias


conteo_categorias = {"Acceso": 0, "Equipo": 0, "Red": 0}
total_minutos = 0
pendientes = 0
provincias_pendientes = set()
urgentes = []
caso_mas_largo = ("", 0)
# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
print("ANALISIS")


# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.

# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
for inc in incidencias:

    
    total_minutos += inc["minutos_atencion"]


    conteo_categorias[inc["categoria"]] += 1
    if not inc["resuelto"]:
        pendientes += 1
        provincias_pendientes.add(inc["provincia"])
        
        if inc["minutos_atencion"] >= 60:
            urgentes.append((inc["id"], inc["minutos_atencion"]))
    
    if inc["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (inc["id"], inc["minutos_atencion"])


promedio = total_minutos / len(incidencias)


# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
print("Total de minutos:", total_minutos)
print("Promedio de minutos:", promedio)
print("Conteo por categoría:", conteo_categorias)
print("Casos pendientes:", pendientes)
print("Provincias con pendientes:", provincias_pendientes)
print("Casos urgentes:", urgentes)
print("Caso más largo:", caso_mas_largo)

if "San Jose" in provincias_pendientes:
    print("Hay pendientes en San Jose.")
else:
    print("No hay pendientes en San Jose.")