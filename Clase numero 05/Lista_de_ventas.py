#ventas viernes, sabado, domingo
#ventas_fin_semana = llamado dato original
ventas_fin_semana = [125000, 98000, 150000]

total_ventas= sum(ventas_fin_semana)

print(f"Total de ventas: {total_ventas:.2f}")

venta_minima = min(ventas_fin_semana)

venta_maxima = max(ventas_fin_semana)

print("venta minima:", venta_minima)
print("venta maxima:", venta_maxima)