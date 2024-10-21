import random

numAdivinar = random.randint(1, 100)
num = int(0)
while (num != numAdivinar):
    num = int(input("Inserta un numero: "))
    if num == numAdivinar:
        print("GG")
    elif num > numAdivinar:
        print("Menor")
    else:
        print("Mayor")