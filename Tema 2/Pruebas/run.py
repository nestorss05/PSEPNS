from random import randint
from multiprocessing import Process, Pipe

def pideNumero():
    num = int(input('Ingrese un numero: '))
    return num

def sorteo(pipe):
    lista=[]
    while True:
        if pipe.recv()==0:
            numero = randint(1, 100)
            while numero in lista:
                lista.append(numero)
            print(f"Sorteing... {numero}")
            pipe.send(numero)
        else:
            break

def jugador(pipe, num):
    creditos = 10
    print("Nummer: ", num)
    while creditos > 0:
        pipe.send(0)
        creditos-=1
        elegido = pipe.recv()
        if int(elegido)==num:
            print("GG")
            pipe.send(1)
            break
        else:
            print("PUTA")
    if creditos == 0:
        print("BUAAAHHH BUAAAHHHH")
        pipe.send(1)
    pipe.close()

if __name__ == '__main__':
    numero = pideNumero()
    pipe1, pipe2 = Pipe()
    p1 = Process(target=sorteo, args=(pipe1,))
    p2 = Process(target=jugador, args=(pipe2,numero))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Finiquitao final')