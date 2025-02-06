import random
import time
from threading import Thread

TRABAJADORES = 5

class Trabajadores(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            print(f"Soy {self.name} y estoy trabajando")
            time.sleep(random.randint(1, 10))
            print(f"Soy {self.name} y he terminado de trabajar")

if __name__ == "__main__":
    print("Boletin 1 - Ejercicio 1")
    threads = []

    for i in range(TRABAJADORES):
        t = Trabajadores(i+1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()