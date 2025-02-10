import random
import time
from threading import Condition, Thread, Barrier

INTENTOS = 10
Acertado = False

class Numero:
    def __init__(self, barrier):
        self.numero = random.randint(0, 100)
        self.cond = Condition()
        self.barrier = barrier
        self.idac = ""

    def adivinar_numero(self, nombre):
        global Acertado
        self.barrier.wait()

        while not Acertado:
            numero = random.randint(0, 100)

            with self.cond:
                if Acertado:
                    break

                if numero == self.numero:
                    print(f"({nombre}) MIO!!! (numero: {numero})")
                    Acertado = True
                    self.idac = nombre
                    self.cond.notify_all()
                    break
                else:
                    print(f"({nombre}) No acerte (numero: {numero})")

            time.sleep(random.uniform(0.05, 0.20))

        if self.idac != nombre:
            print(f"({nombre}) Mierda, ya acerto")

class Intentador(Thread):
    def __init__(self, nombre, numero):
        Thread.__init__(self, name=nombre)
        self.numero = numero

    def run(self):
        self.numero.adivinar_numero(self.name)

if __name__ == '__main__':
    barrier = Barrier(INTENTOS)
    numero = Numero(barrier)
    hilos = []

    for i in range(INTENTOS):
        intnt = Intentador(str(i+1), numero)
        hilos.append(intnt)
        intnt.start()

    for h in hilos:
        h.join()