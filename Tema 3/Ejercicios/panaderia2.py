import random
from threading import Thread, Lock, Semaphore
import time

class Panaderia(Thread):
    barras = 7
    venta = Lock()

    def __init__(self):
        Thread.__init__(self)

    def compra_pan(self):
        self.venta.acquire()
        if self.barras > 0:
            self.barras -= 1
            ok = True
        else:
            print("NO PAN")
            ok = False
        self.venta.release()
        return ok

class Comprador(Thread):
    def __init__(self, panaderia, num):
        Thread.__init__(self)
        self.panaderia = panaderia
        self.num = num

    def run(self):
        print("PAN COMPRA", self.num)
        time.sleep(random.randint(1, 3))
        if self.panaderia.compra_pan():
            print("COMPRO PAN GG", self.num)
        else:
            print("Nein", self.num)

if __name__ == "__main__":
    print("La panaderia")
    pan = Panaderia()
    for i in range(10):
        c = Comprador(pan, i)
        c.start()