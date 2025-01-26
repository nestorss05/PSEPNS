import random
from threading import Semaphore, Thread, Lock
import time

MAX = 5
PERS = 20

class Puente:
    def __init__(self):
        self.sentidoActual = None
        self.lock = Lock()
        self.sentido1 = Semaphore(MAX)
        self.sentido2 = Semaphore(MAX)
        self.waitlist1 = 0
        self.waitlist2 = 0

    def entrada(self, sentido, nombre):
        with self.lock:
            if sentido:
                self.waitlist1 += 1
            else:
                self.waitlist2 += 1

            while self.sentidoActual is not None and self.sentidoActual != sentido:
                self.lock.release()
                time.sleep(0.01)
                self.lock.acquire()

            if self.sentidoActual is None:
                self.sentidoActual = sentido

            if sentido:
                self.waitlist1 -= 1
            else:
                self.waitlist2 -= 1

        if sentido:
            self.sentido1.acquire()
        else:
            self.sentido2.acquire()

        print(f"El coche {nombre} entra al puente (sentido {sentido})")

    def cruce(self, nombre):
        print(f"El coche {nombre} cruza epicamente el puente")
        time.sleep(random.uniform(1, 5))

    def salida(self, sentido, nombre):
        print(f"El coche {nombre} efectua su salida del puente (sentido {sentido})")

        if sentido:
            self.sentido1.release()
        else:
            self.sentido2.release()

        with self.lock:
            if (sentido and self.sentido1._value == MAX) or (not sentido and self.sentido2._value == MAX):
                print("Puente libre")
                self.sentidoActual = None

                if self.waitlist1 > 0 and self.sentido2._value == MAX:
                    self.sentidoActual = True
                    print("VIA LIBRE, VIA 1")
                elif self.waitlist2 > 0 and self.sentido1._value == MAX:
                    self.sentidoActual = False
                    print("VIA LIBRE, VIA 2")

class Vehiculo(Thread):
    def __init__(self, nombre, sentido, puente):
        Thread.__init__(self, name=nombre)
        self.puente = puente
        self.sentido = sentido

    def run(self):
        print(f"El coche {self.name} va al puente (sentido {self.sentido})")
        self.puente.entrada(self.sentido, self.name)
        self.puente.cruce(self.name)
        self.puente.salida(self.sentido, self.name)

if __name__ == '__main__':
    print("Puente España")
    puente = Puente()
    threads = []

    for i in range(1, PERS + 1):
        sentido = random.choice([True, False])
        vehiculo = Vehiculo(str(i), sentido, puente)
        threads.append(vehiculo)
        vehiculo.start()
        time.sleep(random.uniform(0.5, 2))

    for t in threads:
        t.join()