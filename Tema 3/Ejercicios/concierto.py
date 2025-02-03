import random
import time
from threading import Thread, Event

tickets = 20

class Empresa(Thread):
    def __init__(self, event:Event):
        Thread.__init__(self)
        self.event = event
        self.tocacoshouns = 0

    def run(self):
        self.event.clear()
        print("(General) Taquilla activa")
        time.sleep(5)
        print("(General) CIERRENLA")
        self.event.set()

    def compra_entradas(self, nombre):
        if not self.event.is_set():
            print(f"({nombre}) Comprando entradas...")
            time.sleep(random.randint(2, 4))
            print(f"({nombre}) Entradas compradas")
        else:
            if self.tocacoshouns == (tickets / 2):
                print(f"({nombre}) QUE NO, QUE ESTA CERADO, CONIO")
            else:
                print(f"({nombre}) Esta cerado senior, lo siento mucho.")
                self.tocacoshouns += 1

class Comprador(Thread):
    def __init__(self, nombre, empresa: Empresa):
        Thread.__init__(self, name=nombre)
        self.empresa = empresa

    def run(self):
        print(f"({self.name}) Se ha entrado en el proceso")
        empresa.compra_entradas(self.name)
        print(f"({self.name}) Se termino el proceso")

if __name__ == '__main__':
    print("Enga, tickets a mitad de precio (Modo Online)")
    event = Event()
    empresa = Empresa(event)
    empresa.start()
    threads = []

    for i in range(tickets):
        e = Comprador(f"T{i}", empresa)
        time.sleep(random.uniform(0.5, 1.2))
        threads.append(e)
        e.start()

    for t in threads:
        t.join()