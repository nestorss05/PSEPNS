def main():
    cont = int(0)
    numeros = []

    while cont < 10:
        cont = cont + 1
        numero = int(input("Inserta un numero:"))
        numeros.append(numero)

    numeros.sort()
    print(numeros)

if __name__ == "__main__":
    main()