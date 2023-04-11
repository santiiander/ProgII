
def pila_vacia(pila, tope):
    if tope == 0:
        band = True
    else:
        band = False
    return band

def pila_llena(pila, tope, max):
    if tope == max:
        band = True
    else:
        band = False
    return band

def poner_dato(pila, tope, max, dato):
    band = pila_llena(pila, tope, max)
    if band == True:
        print("Desbordamiento - Pila llena")
    else:
        dato = int(input("Ingrese el dato numérico a insertar: "))
        pila.append(dato)
        tope += 1
    return tope
def quitar_dato(pila, tope, max):
    band = pila_vacia(pila, tope)
    if band == True:
        print("Subdesbordamiento - Pila vacía")
    else:
        tope -= 1
        pila[tope] = 0
    return tope
def mostrar_elementos(pila):
    print("La fila tiene los siguientes elementos: ")
    print("Posición 11: ", pila[10])
    print("Posición 10: ", pila[9])
    print("Posición 9: ", pila[8])
    print("Posición 8: ", pila[7])
    print("Posición 7: ", pila[6])
    print("Posición 6: ", pila[5])
    print("Posición 5: ", pila[4])
    print("Posición 4: ", pila[3])
    print("Posición 3: ", pila[2])
    print("Posición 2: ", pila[1])
    print("Posición 1: ", pila[0])


max = 11
tope = 0
dato = 0
pila = [] * max
band = False

seleccion = 1

while seleccion == 1 or seleccion == 2 or seleccion == 3 or seleccion == 4 or seleccion == 5:
    print(f"Seleccione que desea hacer con la estructur pila (Tope = {tope})")
    print("1- Saber si la pila está vacía.")
    print("2- Saber si la pila está llena.")
    print("3- Colocar un elemento a la pila.")
    print("4- Quitar un elemento a la pila.")
    print("5- Mostrar los elementos actuales de la pila.")
    print("Cualquier otro número - Salir.")
    seleccion = int(input("Ingrese su selección: "))
    if seleccion == 1:
        band = pila_vacia(pila, tope)
        if band == True:
            print("La pila está vacía.")
        else:
            print("La pila no está vacía.")
    elif seleccion == 2:
        band = pila_llena(pila, tope, max)
        if band == True:
            print("La pila está llena.")
        else:
            print("La pila está vacía.")
    elif seleccion == 3:
        tope = poner_dato(pila, tope, max, dato)
    elif seleccion == 4:
        tope = quitar_dato(pila, tope, max)
    elif seleccion == 5:
        mostrar_elementos(pila)
    elif seleccion != 1 and seleccion != 2 and seleccion != 3 and seleccion != 4 and seleccion != 5:
        print("Hasta luego.")

#VER USAR MATCH