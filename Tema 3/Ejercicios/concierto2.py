import random
import time
from threading import Thread, Event, Lock

tickets = 15

## WIP

class Empresa(Thread):
    def __init__(self, event:Event, bloqueo: Lock):
        Thread.__init__(self)
        self.event = event
        self.bloqueo = bloqueo
        self.tocacoshouns = 0
        self.compracion = True

    def run(self):
        print("(General) Taquilla activa")
        time.sleep(5)
        print("(General) CIERRENLA")
        bloqueo.acquire()

    def compra_entradas(self, nombre):
        if not bloqueo.locked():
            while not self.event.is_set():
                print(f"({nombre}) Renta esperar un poquito la cola")
                self.compracion = self.event.wait(2)

            if self.compracion:
                self.event.clear()
                print(f"({nombre}) Comprando entradas...")
                time.sleep(random.randint(4, 5))
                print(f"({nombre}) Entradas compradas")
                self.event.set()
            else:
                print(f"({nombre}) Yo no comprar")

        else:
            if self.tocacoshouns == (tickets / 3):
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
    print("Enga, tickets a mitad de precio (Modo Taquilla)")
    bloqueo = Lock()
    event = Event()
    event.set()
    empresa = Empresa(event, bloqueo)
    empresa.start()
    threads = []

    for i in range(tickets):
        e = Comprador(f"T{i}", empresa)
        time.sleep(random.uniform(0.4, 1.1))
        threads.append(e)
        e.start()

    for t in threads:
        t.join()