def main():
    numeros = []
    f1 = open('ficheroR.txt', 'r')
    for linea in f1.readlines():
        palabras = linea.split("\n")
        numeros.append(palabras[0])
    numeros.sort()
    f2 = open('ficheroW.txt', 'w') 
    for numero in numeros:
        f2.write(str(numero) + "\n")

if __name__ == "__main__":
    main()