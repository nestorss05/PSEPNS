import random
from threading import Lock, Thread, Barrier

INTENTOS = 10
Acertado = False

class Numero:
    def __init__(self, barrier):
        self.numero = random.randint(0, 100)
        self.lock = Lock()
        self.barrier = barrier
        self.idac = ""

    def adivinar_numero(self, nombre):
        global Acertado
        self.barrier.wait()

        while not Acertado:
            numero = random.randint(0, 100)

            if numero == self.numero:
                print(f"({nombre}) MIO!!! (numero: {numero})")
                Acertado = True
                if not self.lock.locked():
                    self.lock.acquire()
                break
            else:
                print(f"({nombre}) No acerte (numero: {numero})")

            random.uniform(0.5, 1.0)

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