def main():

    def leerNums(numA, numB):
        if numA < numB:
            cont = cont + 1
            for cont in range(numA, numB):
                print(str(cont))
        else:
            cont = cont + 1
            for cont in range(numB, numA):
                print(str(cont))

    num1 = int(input("Dime numero 1: "))
    num2 = int(input("Dime numero 2: "))

    leerNums(num1, num2)

if __name__ == "__main__":
    main()