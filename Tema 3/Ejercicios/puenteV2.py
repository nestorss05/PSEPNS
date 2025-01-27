import random
from threading import Semaphore, Thread
import time

MAX = 1
PERS = 10

class Puente(Thread):

## Se ha usado la correccion de Jose Luis

    sentido1 = Semaphore(MAX)
    sentido2 = Semaphore(MAX)

    def __init__(self, nombre, direccion):
        Thread.__init__(self, name=nombre)
        self.direccion = direccion

    def run(self):

        if self.direccion == True:
            self.sentido1.acquire()
            self.sentido2.acquire()
            print(f"{self.name} esta cruzando el puente (Sentido 1)")
            time.sleep(random.randint(2, 3))
            print(f"{self.name} acaba de cruzar el puente (Sentido 1)")
            self.sentido1.release()
            self.sentido2.release()
        else:
            self.sentido2.acquire()
            self.sentido1.acquire()
            print(f"{self.name} esta cruzando el puente (Sentido 2)")
            time.sleep(random.randint(2, 3))
            print(f"{self.name} acaba de cruzar el puente (Sentido 2)")
            self.sentido2.release()
            self.sentido1.release()

if __name__ == "__main__":
    print("Puente España")

    for i in range(1, PERS + 1):
        sentido = random.choice([True, False])
        vehiculo = Puente(str(i), sentido)
        vehiculo.start()
        vehiculo.join()
        time.sleep(random.uniform(0.5, 1))