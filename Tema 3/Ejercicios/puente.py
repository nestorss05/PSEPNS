import random
from threading import Semaphore, Thread
import time

MAX = 5
PERS = 20
entrado = False
sentidoActual = False

class Puente(Thread):
    sentido = None
    sentido1 = Semaphore(MAX)
    sentido2 = Semaphore(MAX)
    pers = 0

    def __init__(self, nombre, sentido):
        Thread.__init__(self, name=nombre)
        self.sentido = sentido

    def run(self):
        print(f"El coche {self.name} va al puente")
        if self.sentido is True:
            self.sentido1.acquire()
        else:
            self.sentido2.acquire()
        if not entrado:
            print("Que entre uno de los sentidos")
            sentidoActual = self.sentido
        ## TODO: terminar

if __name__ == '__main__':
    print("Puente España")
    for i in range(1, PERS + 1):
        suerte = random.randint(0, 2)
        res = True
        if suerte == 0: res = False
        t = Puente(str(i), res)
        t.start()