def main():

    def sumar(numA, numB):
        return float(numA + numB)

    def restar(numA, numB):
        return float(numA - numB)

    def multiplicar(numA, numB):
        return float(numA * numB)

    def dividir(numA, numB):
        return float(numA / numB)

    opc = int(5)
    while opc != 0:
        num1 = int(input("Inserta un numero: "))
        num2 = int(input("Inserta otro numero: "))
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Salir")
        opc = int(input("Elige una opcion: "))
        if opc == 1:
            print(str(sumar(num1, num2)))
        elif opc == 2:
            print(str(restar(num1, num2)))
        elif opc == 3:
            print(str(multiplicar(num1, num2)))
        elif opc == 4:
            print(str(dividir(num1, num2)))
        elif opc == 0:
            print("Saliendo...")
        else:
            print("ERROR: opcion invalida")

if __name__ == "__main__":
    main()