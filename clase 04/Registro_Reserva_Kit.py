#Registro_Reserva_Kit.py
#solucion Kit seguro
#autor: Ronny Villalobos duarte F:2026/10/06

nombre = input("Nombre : ").strip().upper()
kit = input("Tipó de Kit : ").strip().lower()
autorizacion = input("Tiene autorizacion? ").strip().lower() == "si"

#cantidad = int(input("Ingrese la Cantidad: "))

try:
    cantidad = int(input("Ingrese la Cantidad: "))
    pass #La tarea

except ValueError:
   print("Error cantidad invalida, asignada -1")
   cantidad = -1
   
try:
     dias = int(input("Dias de prestamo: "))
except ValueError:
    print("Lo dias no estan en el formato correcto")
    dias = -1
    resultado =""
if not nombre == "" or  kit  or cantidad <= 1 or dias <= 1:
    resultado = "Registro Rechazado: Datos invalidos "
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"Solicitud Aprovado para {nombre}:{cantidad} kit (s)de {kit})."
elif cantidad > 3 or dias > 7:
     resultado = "Solicitud enviada a revisión!"
else:
    resultado = "Solicitud rechazada: se requiere autorización"
    
print(resultado)

 
