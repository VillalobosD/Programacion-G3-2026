"""Microreto: el portero del café."""

energia = int(input("Ingrese Cuanta Energia tienes de 0 a 100?: "))
cafe = input("Traes cafe si / no: ").lower().strip() == "si"

#energia = 
#trae_cafe = input("¿Traes café? (si/no): ")

mensaje = "Completa las reglas del portero."

# TODO: usa and para detectar energía baja sin café.
if energia < 30 and not(cafe):
    mensaje = "Vaya a Dormir"
    
# TODO: usa or para permitir energía suficiente o café.
elif energia >= 30 or cafe:
    mensaje = "Pasa por el cafe"
# TODO: escribe mensajes claros para cada resultado.
else:
    mensaje = "El guarda esta pensando si  te deja entrar"()


print(mensaje)

