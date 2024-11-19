from random import randint
from multiprocessing import Process, Queue
from time import sleep

def pideNumero():
    num = int(input('Ingrese un numero: '))
    return num

def sorteo(queue):
    lista=[]
    while True:
        mensaje = queue.get()
        if mensaje != "FIN":
            numero = randint(1, 100)
            while numero in lista:
                numero = randint(1, 100)
            lista.append(numero)
            print(f"Sorteing... {numero}")
            queue.put(numero)
        else:
            break
        sleep(1)

def jugador(queue, num, jugador):
    creditos = 10
    print("Numero: ", num)
    print("Jugador: ", jugador)
    while creditos > 0:
        queue.put("PEDIR")
        elegido = queue.get()
        if elegido==num:
            print(f"{jugador}: GG")
            queue.put("FIN")
            break
        else:
            print(f"{jugador}: PUTA")
        creditos -= 1
        sleep(2)
    if creditos == 0:
        print("BUAAAHHH BUAAAHHHH")
        queue.put("FIN")
    print(f"{jugador} ha terminado")

if __name__ == '__main__':
    numero1 = pideNumero()
    numero2 = pideNumero()
    queue = Queue()
    p1 = Process(target=sorteo, args=(queue,))
    p2 = Process(target=jugador, args=(queue, numero1, "Pepe"))
    p3 = Process(target=jugador, args=(queue, numero2, "Sech"))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('Finiquitao final')