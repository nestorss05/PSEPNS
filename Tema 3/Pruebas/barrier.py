import random
import time
from threading import Barrier, Thread

DERRUMBE = 5

class Caja(Thread):
    def __init__(self, nombre, barrera: Barrier):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera

    def run(self):
        print(f"Hilos que derrumbaran la caja: {self.barrera.n_waiting + 1} / {DERRUMBE}")
        self.barrera.wait()
        print(f"Hilo {self.name} entra en caja")
        time.sleep(random.randint(1,3))
        print(f"Hilo {self.name} sale en caja")

if __name__ == "__main__":
    barrera = Barrier(DERRUMBE)
    hilos = []

    for i in range(10):
        hilo = Caja(str(i), barrera)
        time.sleep(random.randint(1,3))
        hilo.start()
        hilos.append(hilo)

    for h in hilos:
        h.join()