import random
import time
from threading import Thread, Event, Semaphore

PEATONES = 20

class Semaforo(Thread):
    def __init__(self, event: Event):
        Thread.__init__(self)
        self.event = event
        self.peatones = 0

    def pasados(self):
        self.peatones += 1

    def run(self):
        while self.peatones < PEATONES:
            print("Luz verde")
            self.event.set()
            time.sleep(3)
            print("Luz roja")
            self.event.clear()
            time.sleep(5)

class Peaton(Thread):

    semaphore = Semaphore(int(PEATONES / 4))

    def __init__(self, nombre, semaforo):
        Thread.__init__(self, name=nombre)
        self.semaforo = semaforo

    def run(self):
        Peaton.semaphore.acquire()
        while not self.semaforo.event.is_set():
            print(f"({self.name}) Esperando...")
            self.semaforo.event.wait()
        print(f"({self.name}) Pasando...")
        time.sleep(random.randint(1, 2))
        print(f"({self.name}) Hecho")
        self.semaforo.pasados()
        Peaton.semaphore.release()

if __name__ == "__main__":
    print("Simulador de paso de peatones")
    threads = []
    e = Event()
    s = Semaforo(e)
    s.start()

    for i in range(PEATONES):
        p = Peaton(f"Peaton {i}", s)
        threads.append(p)
        p.start()

    for t in threads:
        t.join()