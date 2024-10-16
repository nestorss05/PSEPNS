def main():

    def esVocal(carac):
        esValido = False
        if carac == 'A' or carac == 'E' or carac == 'I' or carac == 'O' or carac == 'U':
            esValido = True
        return esValido

    character = input("Inserta un caracter: ")
    print(esVocal(character.upper()))

if __name__ == "__main__":
    main()