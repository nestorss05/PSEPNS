longitud = int(input("Inserta la longitud del triangulo: "))
if longitud >= 1:
    for i in range(longitud):
        for j in range(longitud):
            if j+i<longitud-1:
                print(" ", end="")
            else:
                print("* ", end="")
        print()
else:
    print("ERROR: longitud negativa o invalida")