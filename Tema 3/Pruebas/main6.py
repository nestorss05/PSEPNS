import random
from threading import Semaphore, Thread
import time

class Supermercado(Thread):
    semaforo = Semaphore(4)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"Hilo {self.name} vauna caha")
        Supermercado.semaforo.acquire()
        print(f"Hilo {self.name} ta ziendoa tendio")
        time.sleep(random.randint(1,10))
        print(f"Hilo {self.name} ta pagando")
        Supermercado.semaforo.release()
        print(f"Hilo {self.name} abandonaer zupermercao")

if __name__ == "__main__":
    print("Soy el hilo principal")
    for i in range(1, 10):
        t = Supermercado(str(i))
        t.start()