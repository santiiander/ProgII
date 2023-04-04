confirm=("xd")
with open('C:\\Users\\santiago\\Desktop\\prueba\\holaxd','w') as holaxd:
    while confirm!="fin":
        confirm=str(input("Ingrese lo que quiera ingresar a la linea o fin para terminar"))
        holaxd.write(confirm+"\n")