# 1. Entrada de datos fijos (Texto)
nombre = input("Ingrese su nombre: ").upper().strip()

# 2. Inicialización del acumulador
descuento = 0.0

# 3. Bloque seguro para evitar caídas del programa por datos inválidos
try:
    # Pedimos de forma segura los valores numéricos
    monto_original = float(input("Ingrese el monto de la compra: "))
    veces = int(input("Ingrese la cantidad de veces que compra: "))
    
    # Evaluamos las condiciones de arriba a abajo
    if monto_original >= 100000:
        descuento = monto_original * 0.10
        
    elif monto_original >= 50000 and monto_original < 100000:
        # ¿Qué cálculo de descuento va aquí? 
        
    elif veces > 5:
        # ¿Qué cálculo de descuento va aquí si compra más de 5 veces?
        
    else:
        # Si no cumple ninguna condición
        descuento = 0.0

except ValueError: # Captura si ingresan letras
    print("Error: Solo se permiten números enteros para visitas y decimales para montos.")
    # Si hay error, nos aseguramos de que el descuento quede en 0 para que no falle el cálculo final
    descuento = 0.0
    monto_original = 0.0

# 4. Salida de resultados (Solo si el monto original es mayor a 0)
if monto_original > 0:
    print(nombre, f"El descuento es de: {descuento}")
    print(nombre, f"El total a pagar es: {monto_original - descuento}")