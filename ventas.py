# Pedir el número de sucursales y de meses
num_sucursales = int(input("Ingrese el número de sucursales: "))
num_meses = int(input("Ingrese el número de meses: "))

# Pedir las ventas de cada sucursal y de cada mes
ventas = []
for i in range(num_sucursales):
    ventas_sucursal = []
    for j in range(num_meses):
        venta = float(input(f"Ingrese las ventas de la sucursal {i+1} en el mes {j+1}: "))
        ventas_sucursal.append(venta)
    ventas.append(ventas_sucursal)

# Calcular el total de ventas de la compañía
total_ventas = sum(sum(fila) for fila in ventas)

# Calcular el total de ventas por cada sucursal
ventas_por_sucursal = [sum(fila) for fila in ventas]

# Encontrar la sucursal que más vendió durante el año
indice_sucursal_mas_vendida = ventas_por_sucursal.index(max(ventas_por_sucursal))
sucursal_mas_vendida = f'Sucursal {indice_sucursal_mas_vendida + 1}'

# Encontrar el mes que menos vendió la compañía
total_ventas_por_mes = [sum(columna) for columna in zip(*ventas)]
indice_mes_menos_vendido = total_ventas_por_mes.index(min(total_ventas_por_mes))
mes_menos_vendido = indice_mes_menos_vendido + 1

# Imprimir los resultados
print(f'Total de ventas de la compañía: {total_ventas}')
for i, ventas_sucursal in enumerate(ventas_por_sucursal):
    print(f'Total de ventas de la Sucursal {i+1}: {ventas_sucursal}')
print(f'Sucursal que más vendió durante el año: {sucursal_mas_vendida}')
print(f'Mes que menos vendió la compañía: {mes_menos_vendido}')
