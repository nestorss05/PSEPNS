from multiprocessing import Process

def ejercicio(num: int, proc: int):
    print("Proceso nº", proc)
    numFinal = 0
    for i in range(1,num+1):
        numFinal += i
        print("Suma de todos los valores hasta el 1: " + str(numFinal))
    return numFinal

if __name__ == "__main__":
    num = int(input("Inserta un numero: "))
    proceso1 = Process(target=ejercicio, args=(num, 1))
    proceso2 = Process(target=ejercicio, args=(num, 2))
    proceso1.start()
    proceso2.start()
    proceso1.join()
    print("Proceso 1 terminado")
    proceso2.join()
    print("Proceso 2 terminado")