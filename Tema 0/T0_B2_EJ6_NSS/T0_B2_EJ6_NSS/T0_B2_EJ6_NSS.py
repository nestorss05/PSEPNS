def main():
    palabras=[]
    diccionario={}
    cadena = input("Inserta una frase: ")
    palabras = cadena.split(' ')

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    print(diccionario)

if __name__ == "__main__":
    main()