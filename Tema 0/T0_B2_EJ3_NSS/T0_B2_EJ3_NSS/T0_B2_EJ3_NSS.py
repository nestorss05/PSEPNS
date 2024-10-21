def main():
    cont = int(0)
    numeros = []
    add = ""
    while (cont < 8):
        cont = cont + 1
        num = int(input("Inserta un numero: "))
        numeros.append(num)
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            add = ": par"
        else:
            add = ": impar"
        print(str(numeros[i]) + add)

if __name__ == "__main__":
    main()