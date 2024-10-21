def main():
    f = open('fichero.txt', 'w')
    cadena = input("Inserta un texto: ")
    if (cadena != "fin"):
        f.write(cadena + "\n")
    while (cadena != "fin"):
        cadena = input("Inserta un texto: ")
        if (cadena != "fin"):
            f.write(cadena + "\n")

if __name__ == "__main__":
    main()