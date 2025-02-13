import random
import time
from threading import Thread, Barrier, Timer

COCHES = 10

class Anuncier(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.anuncier = False
        self.passer = False
        self.pos = 0

    def preparacionFinal(self):
        if not self.anuncier:
            self.anuncier = True
            print("Preparados, listos...")

    def inicioFinal(self):
        if not self.passer:
            self.passer = True
            print("YA!!!")

    def llegada(self):
        self.pos += 1
        return self.pos

class Coche(Thread):
    def __init__(self, nombre, barrera, anuncier):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera
        self.anuncier = anuncier

    def iniciarCarrera(self):
        self.anuncier.inicioFinal()
        self.contenidoCarrera()

    def contenidoCarrera(self):
        print(f"El coche {self.name} sale de la salida!")
        time.sleep(random.randint(2, 5))
        print(f"El coche {self.name} va a mitad de recorrido")
        time.sleep(random.randint(2, 5))
        print(f"El coche {self.name} esta a punto de llegar")
        time.sleep(random.randint(2, 5))
        pos = self.anuncier.llegada()
        print(f"El coche {self.name} ha llegado a la meta! (pos. {pos} / {COCHES})")

    def run(self):
        print(f"Se ha unido el coche {self.name}: {self.barrera.n_waiting + 1} / {COCHES}")
        self.barrera.wait()
        t = Timer(3, self.iniciarCarrera)
        t.start()
        self.anuncier.preparacionFinal()

if __name__ == "__main__":
    barrera = Barrier(COCHES)
    anuncier = Anuncier()
    Threads = []

    for i in range(COCHES):
        c = Coche(str(i+1), barrera, anuncier)
        Threads.append(c)
        c.start()

    for t in Threads:
        t.join()