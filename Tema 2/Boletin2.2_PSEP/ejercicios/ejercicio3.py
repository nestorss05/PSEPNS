from multiprocessing import Queue, Process
from time import sleep

def producer(num: int, queue: Queue, proc: int):
    print("PROCESO " + str(proc))
    numFinal = 0
    for i in range(1,num+1):
        numFinal += i
        queue.put(numFinal)
        print(numFinal, "Enviado")
        sleep(1)
    queue.put(None)

def consumer(queue: Queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print("Suma de todos los valores hasta el 1: " + str(item))
    sleep(2)

if __name__ == "__main__":
    num = int(input("Inserta un numero: "))
    queue = Queue()
    proceso1a = Process(target=producer, args=(num, queue, 1))
    proceso1b = Process(target=consumer, args=(queue,))
    proceso2a = Process(target=producer, args=(num, queue, 2))
    proceso2b = Process(target=consumer, args=(queue,))
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