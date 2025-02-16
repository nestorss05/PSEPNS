import random
import time
from threading import Thread, Barrier, Event

TRABAJADORES = 5

class Trabajador(Thread):
    def __init__(self, nombre, barrera: Barrier, pedidos: Event):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera
        self.pedidos = pedidos

    def run(self):
        print(f"({self.name}) Trabajador esperando a los demas...")
        self.barrera.wait()
        print(f"({self.name}) Trabajador empieza su chamba en la factoria")

        while True:
            print(f"({self.name}) Esperando un pedido...")
            self.pedidos.wait()
            print(f"({self.name}) Procesando un pedido...")
            time.sleep(random.uniform(1, 3))
            print(f"({self.name}) Pedido completado.")

class Generador(Thread):
    def __init__(self, pedidos: Event):
        Thread.__init__(self)
        self.pedidos = pedidos
        self.activo = True

    def run(self):
        while self.activo:
            print("(Generador) Regenerando...")
            time.sleep(random.uniform(2, 5))
            print("(Generador) Se ha generado un nuevo pedido.")
            self.pedidos.set()
            time.sleep(1)
            self.pedidos.clear()

    def detener(self):
        print("(Generador) Deteniendo el generador...")
        self.activo = False

if __name__ == "__main__":
    print("Simulador de procesamiento de pedidos")
    barrera = Barrier(TRABAJADORES)
    pedidos = Event()
    threads = []

    for i in range(TRABAJADORES):
        t = Trabajador(i+1, barrera, pedidos)
        time.sleep(random.randint(1, 3))
        threads.append(t)
        t.start()

    gen = Generador(pedidos)
    gen.start()

    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("\nDeteniendo el simulador...")
        gen.detener()