import random
from threading import Thread, Condition
import time

MAX = 10

class Panaderia(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.barras = 7
        self.venta = Condition()
        self.panesVendidos = 0

    def compra_pan(self):
        print("Comprando pan...")
        self.barras -= 1
        self.panesVendidos += 1

class Comprador(Thread):

    reponedor = False

    def __init__(self, panaderia, num):
        Thread.__init__(self, name=str(num))
        self.panaderia = panaderia

    def run(self):
        print(f"Hora de comprar pan ({self.name})")
        time.sleep(random.randint(1, 3))
        with self.panaderia.venta:
            while self.panaderia.barras == 0:
                self.panaderia.venta.wait()
            self.panaderia.compra_pan()
            time.sleep(random.randint(1, 3))
            self.panaderia.venta.notify_all()
        print(f"Pan comprado ({self.name})")

class Reponedor(Thread):
    def __init__(self, Panaderia):
        Thread.__init__(self)
        self.p = Panaderia

    def run(self):
        while self.p.panesVendidos < MAX:
            with(self.p.venta):
                while self.p.barras > 0:
                    self.p.venta.wait()
                print("Se esta recargando el pan...")
                time.sleep(random.randint(1, 3))
                self.p.barras = 7
                print("Panes listos")
                self.p.venta.notify_all()

if __name__ == "__main__":
    print("La panaderia")
    pan = Panaderia()
    reponedor = Reponedor(pan)
    reponedor.start()
    lista = []
    for i in range(MAX):
        c = Comprador(pan, i)
        lista.append(c)
        c.start()