import queue
import time
import random
from threading import Thread, Condition

QUEUE = queue.Queue(maxsize=1)
ELEMENTOS = 5
COND = Condition()

class Productores(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"({self.name}) Produciendo...")
        time.sleep(random.randint(1, 3))

        with COND:
            while QUEUE.full():
                print(f"({self.name}) El producto esta listo, pero la cola aun esta llena")
                COND.wait()
            QUEUE.put(f"Producto {self.name} MK-{random.randint(1, 10)}")
            print(f"({self.name}) Para la cola. Ya esta en produccion")
            COND.notify_all()

class Consumidor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        with COND:
            print(f"({self.name}) Esperando a la obtencion...")
            while QUEUE.empty():
                print(f"({self.name}) Cola vacia")
                COND.wait()
            elemento = QUEUE.get()
            print(f"({self.name}) Objeto consumido: {elemento}")
            QUEUE.task_done()
            COND.notify_all()

if __name__ == "__main__":
    print("Productores y consumidores")
    threads1 = []
    threads2 = []

    for i in range(ELEMENTOS):
        producto = Productores(i+1)
        consumidor = Consumidor(i+1)
        threads1.append(producto)
        threads2.append(consumidor)
        producto.start()
        consumidor.start()

    for t1 in threads1:
        t1.join()

    for t2 in threads2:
            t2.join()