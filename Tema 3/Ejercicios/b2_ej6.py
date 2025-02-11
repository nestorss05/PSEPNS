import time
from threading import Thread, Condition
import random

FILOSOFOS = 5
PALILLOS = 5

class Cena(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.palillos = [False] * PALILLOS
        self.cond = Condition()

    def coger_palillos(self, nombre, palillo1, palillo2):
        with self.cond:
            while self.palillos[palillo1] or self.palillos[palillo2]:
                print(f"El filosofo {nombre} esta esperando a que sus palillos esten disponibles")
                self.cond.wait()

            self.palillos[palillo1] = True
            self.palillos[palillo2] = True
            print(f"El filosofo {nombre} ha cogido los palillos {palillo1} y {palillo2}")

    def dejar_palillos(self, nombre, palillo1, palillo2):
        with self.cond:
            self.palillos[palillo1] = False
            self.palillos[palillo2] = False
            print(f"El filosofo {nombre} ha dejado los palillos {palillo1} y {palillo2}")
            self.cond.notify_all()

class Filosofo(Thread):
    def __init__(self, nombre, cena, palillo1, palillo2):
        Thread.__init__(self, name=nombre)
        self.cena = cena
        self.palillo1 = palillo1
        self.palillo2 = palillo2

    def run(self):
        print(f"El filosofo {self.name} va a cenar")
        time.sleep(random.randint(1, 3))
        self.cena.coger_palillos(self.name, self.palillo1, self.palillo2)
        print(f"El filosofo {self.name} esta cenando")
        time.sleep(random.randint(3, 7))
        print(f"El filosofo {self.name} ha terminado de cenar y le tocara volver a pensar")
        self.cena.dejar_palillos(self.name, self.palillo1, self.palillo2)

if __name__ == "__main__":
    print("Problema de los cinco filosofos")
    cena = Cena()
    threads = []

    for i in range(FILOSOFOS):
        palillo1 = i
        if i == FILOSOFOS - 1:
            palillo2 = 0
        else:
            palillo2 = i + 1
        f = Filosofo(str(i), cena, palillo1, palillo2)
        threads.append(f)
        f.start()

    for t in threads:
        t.join()