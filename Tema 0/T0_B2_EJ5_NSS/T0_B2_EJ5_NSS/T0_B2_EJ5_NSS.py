import random

def main():
    numeros = []
    valorN = int # ¿Duda?
    for i in range(100):
        numero = int(random.randint(1, 10))
        numeros.append(numero)
    valorN = int(input("Inserta un numero para mostrar cuantas veces esta: "))
    print("El numero " + str(valorN) + " se repite " + str(numeros.count(valorN)) + " veces en la lista")

if __name__ == "__main__":
    main()