import random
from threading import Semaphore, Thread
import time

MAX = 20
PERS = 50

class Sala(Thread):
    semaforo = Semaphore(MAX)
    pers = 0

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"La persiana namber {self.name} vaal $ine")
        time.sleep(random.randint(1, 5))
        if Sala.pers >= MAX:
            print(f"NOAY ESPASIO PAER {self.name} ENLA SALA")
        Sala.semaforo.acquire()
        Sala.pers += 1
        print(f"La persiana namber {self.name} entroa vela peli (quedan {MAX - Sala.pers} plassa)")
        time.sleep(random.randint(1, 15))
        print(f"La persiana namber {self.name} salio dela peli")
        time.sleep(random.randint(1, 10))
        Sala.semaforo.release()
        Sala.pers -= 1
        print(f"La persiana namber {self.name} hasalio derçine (quedan {MAX - Sala.pers} plassa)")

if __name__ == '__main__':
    print("Andaluçia Çine")
    print(f"Quean: {MAX - Sala.pers} per$iana por entra")
    for i in range(1, PERS+1):
        t = Sala(str(i))
        t.start()