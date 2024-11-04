from time import sleep
from multiprocessing import Process, Queue

def producer(q):
    for i in range(5):
        q.put(i)
        print(i, 'Enviado')
        sleep(2)
    q.put(None)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item, 'Recibido')
    sleep(1)

if __name__ == '__main__':
    queue = Queue()
    proceso1 = Process(target=producer, args=(queue,))
    proceso2 = Process(target=consumer, args=(queue,))
    proceso1.start()
    proceso2.start()
    proceso1.join()
    print('Proceso 1 terminado')
    proceso2.join()
    print('Finiquitao')