from multiprocessing import Pool

def ejercicio(num1: int, num2: int):
    inicio = min(num1, num2)
    fin = max(num1, num2)
    res = sum(range(inicio, fin + 1))
    print(f"Suma entre {inicio} y {fin}: {res}")
    return res

if __name__ == '__main__':
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    with Pool(processes=2) as pool:
        res = pool.starmap(ejercicio, [(num1, num2)])
    print("Ejercicio terminado")
    print(f"El resultado es: {res}")