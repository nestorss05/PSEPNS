def main():
    f = open('datos.txt', 'a')
    nombre = input("Inserta tu nombre: ")
    edad = int(input("Inserta tu edad: "))
    f.write(nombre + " " + str(edad) + "\n")
    f.close()

if __name__ == "__main__":
    main()