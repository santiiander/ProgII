cantAlumnos = int(input("Ingrese la cantidad de alumnos: "))

legajos = []
respuestas = [3, 2, 5, 1, 4, 1, 2, 3, 4, 5]
puntaje = 0
arrayPuntaje = []
resultados = [[0 for col in range(3)] for fila in range(cantAlumnos)]

for i in range(cantAlumnos):
    legajos.append(int(input("Ingrese el legajo del alumno: ")))
    for j in range(3):
        print("Ingrese la respuesta de la pregunta nro ", j+1, " del alumno ", legajos[i])
        resultados[i][j] = int(input())
        if respuestas[j] == resultados[i][j]:
            puntaje += 1
    arrayPuntaje.append(puntaje)
    puntaje = 0

for i in range(cantAlumnos):
    if arrayPuntaje[i]>=2:
        print("Legajo: ", legajos[i], " - APROBADO - ", arrayPuntaje[i])
    else:
        print("Legajo: ", legajos[i], " - DESAPROBADO - ", arrayPuntaje[i])

