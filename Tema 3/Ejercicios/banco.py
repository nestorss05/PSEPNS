import random
from threading import Semaphore, Thread
import time

MAX = 3
PERS = 10

class Cajero(Thread):
    semaforo = Semaphore(MAX)
    pers = 0

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"La persona {self.name} va al cajero")
        time.sleep(random.randint(1, 3))
        if Cajero.pers >= MAX:
            print(f"No quedan cajeros disponibles ({self.name})")
        Cajero.semaforo.acquire()
        Cajero.pers += 1
        print(f"La persona {self.name} empieza a usar el cajero (quedan {MAX - Cajero.pers} cajeros libres)")
        time.sleep(random.randint(1, 20))
        Cajero.semaforo.release()
        Cajero.pers -= 1
        print(f"La persona {self.name} termino de utilizar el cajero (quedan {MAX - Cajero.pers} cajeros libres)")

if __name__ == '__main__':
    print("Banco de España")
    print(f"Quean: {MAX - Cajero.pers} per$iana por entra")
    for i in range(1, PERS + 1):
        t = Cajero(str(i))
        t.start()
