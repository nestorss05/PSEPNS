import random
import time
from threading import Thread, Semaphore

CLIENTES = 10

class Carniceria(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.semaphore = Semaphore(4)

    def atender_cliente(self, num):
        print(f"({num}) quiere entrar a la carniceria")
        self.semaphore.acquire()
        print(f"({num}) Atendiendo cliente...")
        time.sleep(random.randint(1, 5))
        print(f"({num}) Listo")
        self.semaphore.release()

class Cliente(Thread):
    def __init__(self, num, carniceria):
        Thread.__init__(self, name=num)
        self.carniceria = carniceria

    def run(self):
        self.carniceria.atender_cliente(self.name)

if __name__ == "__main__":
    threads = []
    carniceria = Carniceria()
    print("La carniceria")

    for i in range(CLIENTES):
        c = Cliente(str(i+1), carniceria)
        threads.append(c)
        c.start()

    for t in threads:
        t.join()