from multiprocessing import Pool

def ejercicio(num: int):
    numFinal = 0
    for i in range(1,num+1):
        numFinal += i
        print("Suma de todos los valores hasta el 1: " + str(numFinal))
    return numFinal

if __name__ == "__main__":
    num = int(input("Inserta un numero: "))
    with Pool(processes=2) as pool:
        numArray = [num]
        res = pool.map(ejercicio, numArray)
    print("Ejercicio finalizado")
    print("Resultados:", res)