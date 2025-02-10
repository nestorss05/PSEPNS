import random
import time
from threading import Thread, Semaphore

CLIENTES = 10

class Tienda(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.semaphore = Semaphore(4)

    def atender_cliente_carniceria(self, num):
        res = False
        print(f"({num}) quiere entrar a la carniceria")
        if self.semaphore.acquire(timeout=0.5):
            print(f"({num}) Atendiendo cliente... (carniceria)")
            time.sleep(random.randint(1, 5))
            print(f"({num}) Listo (carniceria)")
            self.semaphore.release()
            res = True
        else:
            print(f"({num}) /skip carniceria")
        return res

    def atender_cliente_charcuteria(self, num):
        res = False
        print(f"({num}) quiere entrar a la charcuteria")
        if self.semaphore.acquire(timeout=0.5):
            print(f"({num}) Atendiendo cliente (charcuteria)...")
            time.sleep(random.randint(1, 5))
            print(f"({num}) Listo (charcuteria)")
            self.semaphore.release()
            res = True
        else:
            print(f"({num}) /skip charcuteria")
        return res

class Cliente(Thread):
    def __init__(self, num, tienda):
        Thread.__init__(self, name=num)
        self.tienda = tienda
        self.carni = False
        self.charcu = False

    def run(self):
        final = False
        while not final:
            if not self.carni:
                self.carni = self.tienda.atender_cliente_carniceria(self.name)
            if not self.charcu:
                self.charcu = self.tienda.atender_cliente_charcuteria(self.name)
            if self.carni and self.charcu:
                final = True

if __name__ == "__main__":
    threads = []
    tienda = Tienda()
    print("La carniceria (y charcuteria)")

    for i in range(CLIENTES):
        c = Cliente(str(i+1), tienda)
        threads.append(c)
        c.start()

    for t in threads:
        t.join()