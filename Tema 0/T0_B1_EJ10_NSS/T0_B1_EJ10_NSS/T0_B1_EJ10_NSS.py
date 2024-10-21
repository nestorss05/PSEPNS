def main():
    def numMax(numA, numB):
        max = int(0)
        if numA > numB:
            max = numA
        else:
            max = numB
        return max
    num1 = int(input("Inserta un numero: "))
    num2 = int(input("Inserta otro numero: "))
    print("Numero maximo: " + str(numMax(num1, num2)))

if __name__ == "__main__":
    main()