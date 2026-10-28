#ventas viernes, sabado, domingo
#ventas_fin_semana = llamado dato original
#entrada
ventas_fin_semana = [125000, 98000, 150000]

total_ventas= sum(ventas_fin_semana)
#proceso
print(f"Total de ventas: {total_ventas:.2f}")
venta_minima = min(ventas_fin_semana)
venta_maxima = max(ventas_fin_semana)
#salidas
print("Venta minima:", venta_minima)
print("Venta maxima:", venta_maxima)