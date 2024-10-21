#coding: latin1
def main():
    conjuntos = {"e": "p", "i": "v", "k": "i", "m": "u", "p": "m", "q": "t", "r": "e", "s": "r", "t": "k", "u": "q", "v": "s"}
    frase = input("Inserta una frase: ")
    letras = list(frase.lower())
    for letra in letras:
        if letra in conjuntos:
            letras[letras.index(letra)] = conjuntos[letra]
    frase = ''.join(letras)
    print(frase)

if __name__ == "__main__":
    main()
