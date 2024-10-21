numero = int(input("Inserta un numero entero positivo: "))
cont = int(0)
contP = int(0)
if numero >= 0:
    while cont <= numero:
        cont = cont + 1
        if numero%cont==0:
            contP = contP + 1
    if contP <= 2:
        print("PRIMO")
    else:
        print("NO PRIMO")
else:
    print("ERROR: numero no entero o negativo")