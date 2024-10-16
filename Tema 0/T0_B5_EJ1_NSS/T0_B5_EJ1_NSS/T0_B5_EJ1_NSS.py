def main():
    f = open('Alumnos.txt', 'rt')
    suma = 0
    estatura = 0
    cont = 0
    for linea in f.readlines():
        print(linea, end='')
        palabras = linea.split()
        suma = suma + int(palabras[1])
        estatura = estatura + float(palabras[2])
        cont += 1
    f.close()

    suma = suma / cont
    print("Edad media: " + str(suma))

    estatura = estatura / cont
    print("Estatura media: " + str(estatura))

if __name__ == "__main__":
    main()