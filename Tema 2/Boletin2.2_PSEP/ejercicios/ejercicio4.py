from multiprocessing import Pipe, Process

def producer(num: int, pipe: Pipe, proc: int):
    print("PROCESO " + str(proc))
    numFinal = 0
    for i in range(1,num+1):
        numFinal += i
        pipe.send(numFinal)
        print(numFinal, "Enviado")

def consumer(pipe: Pipe):
    numero = pipe.recv()
    print("Suma de todos los valores hasta el 1: " + str(numero))
    pipe.close()

if __name__ == "__main__":
    num = int(input("Inserta un numero: "))
    pipe1, pipe2 = Pipe()
    proceso1a = Process(target=producer, args=(num, pipe1, 1))
    proceso1b = Process(target=consumer, args=(pipe2,))
    proceso2a = Process(target=producer, args=(num, pipe1, 2))
    proceso2b = Process(target=consumer, args=(pipe2,))
    proceso1a.start()
    proceso1b.start()
    proceso2a.start()
    proceso2b.start()
    proceso1a.join()
    proceso1b.join()
    print("P1 terminado")
    proceso2a.join()
    proceso2b.join()
    print("P2 terminado")