from multiprocessing import Process

def ejercicio(num1: int, num2: int):
    inicio = min(num1, num2)
    fin = max(num1, num2)
    res = sum(range(inicio, fin + 1))
    print(f"Suma entre {inicio} y {fin}: {res}")

if __name__ == '__main__':
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    p1 = Process(target=ejercicio, args=(num1, num2))
    p2 = Process(target=ejercicio, args=(num1, num2))
    p1.start()
    p2.start()
    p1.join()
    print("Proceso 1 terminado")
    p2.join()
    print("Proceso 2 terminado")