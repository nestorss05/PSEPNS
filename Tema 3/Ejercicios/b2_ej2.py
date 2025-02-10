import random
import time
from threading import Thread, Lock

CLIENTES = 5

class Panaderia(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.lock = Lock()

    def atender_cliente(self, num):
        print(f"({num}) quiere entrar a la panaderia")
        self.lock.acquire()
        print(f"({num}) Atendiendo cliente...")
        time.sleep(random.randint(1, 5))
        print(f"({num}) Listo")
        self.lock.release()

class Cliente(Thread):
    def __init__(self, num, panaderia):
        Thread.__init__(self, name=num)
        self.panaderia = panaderia

    def run(self):
        self.panaderia.atender_cliente(self.name)

if __name__ == "__main__":
    threads = []
    panaderia = Panaderia()
    print("La panaderia")

    for i in range(CLIENTES):
        c = Cliente(str(i+1), panaderia)
        threads.append(c)
        c.start()

    for t in threads:
        t.join()