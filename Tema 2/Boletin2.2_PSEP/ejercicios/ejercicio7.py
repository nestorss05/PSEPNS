from multiprocessing import Process, Queue
from time import sleep

def producer(queue: Queue, proc: int):
    print("PROCESO " + str(proc))
    numeros = leeFichero().split(" ")
    queue.put(numeros)
    print("Enviado")
    sleep(1)
    queue.put(None)

def consumer(queue: Queue):
    while True:
        item = queue.get()
        if item is None:
            break
        else:
            num1 = int(item[0])
            num2 = int(item[1])
            inicio = min(num1, num2)
            fin = max(num1, num2)
            res = sum(range(inicio, fin + 1))
            print(f"Suma entre los dos numeros: {res}")
    sleep(2)

def leeFichero():
    archivo = open("../ficheros/ejercicios7y8.txt", "r", encoding="utf-8")
    datos = archivo.read()
    archivo.close()
    return datos

if __name__ == '__main__':
    queue = Queue()
    proceso1a = Process(target=producer, args=(queue, 1))
    proceso1b = Process(target=consumer, args=(queue,))
    proceso2a = Process(target=producer, args=(queue, 2))
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