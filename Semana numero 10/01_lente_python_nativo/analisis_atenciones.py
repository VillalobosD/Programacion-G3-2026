"""Semana 10: resolvemos juntos el caso pendiente de la Semana 9."""

from lector_csv import cargar_atenciones


def explorar_atenciones(atenciones):
    """Decisión 1: ¿qué leímos y cuántas atenciones hay?"""
    # Contamos las filas con un for. Luego miramos los campos de la primera.
    cantidad = 0
    for atencion in atenciones:
        # Completamos aquí el contador.
        cantidad += 1
    print("Atenciones:", cantidad)
    print("Atenciones len():", len(atenciones))
    print("Campos:", list(atenciones[0]))


def contar_categorias(atenciones):
    """Decisión 2: ¿qué medicamentos, hospitales y diagnósticos aparecen?"""
    medicamentos = {}
    hospitales = {}
    diagnosticos = {}

    for atencion in atenciones:
        # Los nombres ya vienen uniformes en el CSV.
        # Contamos cada categoría en su diccionario con .get().
        if atencion["medicamento"] not in medicamentos:
            medicamentos[atencion["medicamento"]] = 0
            medicamentos[atencion["medicamento"]] += 1
        if atencion["hospital"] not in hospitales:
            hospitales[atencion["hospital"]] = 0
        hospitales[atencion["hospital"]] += 1
        if atencion["diagnostico"] not in diagnosticos:
            diagnosticos[atencion["diagnostico"]] = 0
        diagnosticos[atencion["diagnostico"]] += 1

        #get (clave, 0)
        #hospitales[atencion["hospital"]] = hospitales.get(atencion["hospital"], 0) + 1
        #diagnosticos[atencion["diagnostico"]] = diagnosticos.get(atencion["diagnosticos"], 0) + 1



    print("Medicamentos:", medicamentos)
    print("Hospitales:", hospitales)
    print("Diagnósticos:", diagnosticos)


def concluir(atenciones):
    """Decisiones 3 y 4: ¿cuántas personas hay y cuánto esperaron?"""
    visitas = {}
    total_minutos = 0

    for atencion in atenciones:
        cedula = atencion["cedula"]
        visitas[cedula] = visitas.get(cedula, 0) + 1
        minutos = atencion["minutos_espera"]
        total_minutos += minutos
        # Contamos la cédula y acumulamos los minutos de espera.
        

    print("Personas:", len(visitas))
    print("Visitas:", visitas)
    print("Minutos de espera:", total_minutos)
    print("Promedio:", total_minutos / len(atenciones))


atenciones = cargar_atenciones()
if atenciones:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("Revisamos los TODO de lector_csv.py.")
