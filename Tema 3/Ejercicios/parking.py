import random
from threading import Semaphore, Thread
import time

class Parking(Thread):
    semaforo = Semaphore(5)
    i = 0

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"Coshe {self.name} vaal parkin")
        time.sleep(random.randint(1, 5))
        if Parking.i >= 5:
            print(f"NOAY ESPASIO PAER {self.name}")
        Parking.semaforo.acquire()
        Parking.i += 1
        print(f"Coshe {self.name} haaparcao (quedan {5 - Parking.i} plassa)")
        time.sleep(random.randint(1,15))
        print(f"Coshe {self.name} vaa sali")
        time.sleep(random.randint(1, 10))
        Parking.semaforo.release()
        Parking.i -= 1
        print(f"Coshe {self.name} hasalio derparkin (quedan {5 - Parking.i} plassa)")

if __name__ == "__main__":
    print("PARKING ANDALUCIA")
    print(f"Plassa: {5 - Parking.i}")
    for i in range(1, 11):
        t = Parking(str(i))
        t.start()