max_aforo = 700
aforo = 0
aceptados = []
rechazados = []

entrada = input("Ingrese la cantidad de personas de su grupo (o fin para terminar): ").strip().lower()

while entrada != "fin":

    try:
        grupo = int(entrada)

        if grupo <= 0:
            print("Entrada inválida: debe ser un entero mayor que cero.")
        
        else:
            
            if aforo + grupo <= max_aforo:
                print(f"Grupo aceptado: ingresan {grupo} personas.")
                aceptados.append(grupo)
                aforo += grupo
            else:
                print(f"Grupo rechazado: no hay espacio para {grupo} personas.")
                rechazados.append(grupo)

           
            print("Ocupación actual:", aforo)
            print("Espacios disponibles:", max_aforo - aforo)

    except ValueError:
        print("Entrada inválida: debe escribir un número entero o 'fin'.")

    entrada = input("Ingrese la cantidad de personas de su grupo (o fin para terminar): ").strip().lower()


total_admitido = 0
for campos in aceptados:
    total_admitido += campos

# Reporte final
print("Reporte final")
print("Grupos aceptados:", len(aceptados))
print("Grupos rechazados:", len(rechazados))
print("Personas admitidas:", total_admitido)
print("Capacidad máxima:", max_aforo)
print("Espacios disponibles:", max_aforo - total_admitido)