#coding: latin1
def main():
    letras = {"A": 1, "B": 3, "C": 3, "CH": 5, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "L": 1, "LL": 8, "M": 3, "N": 1, "Ñ": 8, "O": 1, "P": 3, "Q": 5, "R": 1, "RR": 8, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8, "Y": 4, "Z": 10}
    letra = input("Inserta una letra: ")
    letra = str(letra.upper())
    if letra in letras:
        print("Puntuacion para la letra " + letra + ": " + str(letras[letra]))
    else:
        print("ERROR: letra no valida o sin puntuacion")

if __name__ == "__main__":
    main()
