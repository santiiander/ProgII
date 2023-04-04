# Crear matriz de 5x5 con ceros
matriz = [[0 for j in range(5)] for i in range(5)]

# Crear listas para llevar un registro de los goles marcados y recibidos por cada equipo
goles_marcados = [0 for i in range(5)]
goles_recibidos = [0 for i in range(5)]

# Llenar matriz con resultados de enfrentamientos ingresados por el usuario
for i in range(5):
    for j in range(5):
        if i != j:
            goles_i = int(input(f"Ingrese la cantidad de goles marcados por Equipo {i+1} en el enfrentamiento contra Equipo {j+1}: "))
            goles_j = int(input(f"Ingrese la cantidad de goles marcados por Equipo {j+1} en el enfrentamiento contra Equipo {i+1}: "))
            resultado = 0
            if goles_i > goles_j:
                resultado = 1
            elif goles_i == goles_j:
                resultado = 0
            elif goles_i < goles_j:
                resultado = -1
            matriz[i][j] = resultado
            goles_marcados[i] += goles_i
            goles_recibidos[i] += goles_j
            goles_marcados[j] += goles_j
            goles_recibidos[j] += goles_i

# Mostrar matriz
print("Matriz de resultados:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()

# Contar triunfos, empates y derrotas de cada equipo y mostrar cantidad total de goles marcados y recibidos
for i in range(5):
    triunfos = 0
    empates = 0
    derrotas = 0
    for j in range(5):
        if matriz[i][j] == 1:
            triunfos += 1
        elif matriz[i][j] == 0:
            empates += 1
        elif matriz[i][j] == -1:
            derrotas += 1
    print(f"Equipo {i+1}: Triunfos: {triunfos}, Empates: {empates}, Derrotas: {derrotas}, Goles Marcados: {goles_marcados[i]}, Goles Recibidos: {goles_recibidos[i]}")

