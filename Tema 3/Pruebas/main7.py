import random
import time
from threading import Thread, Condition


class Lista(Thread):

    lista = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        num = random.randint(0, 4)

        with Lista.cond:
            while Lista.lista[num]:
                print(f"El hilo {self.name} esta esperando a que se libere la posicion {num}")
                Lista.cond.wait()

            Lista.lista[num] = True

        print(f"El hilo {self.name} esta usando el objeto {num}")
        time.sleep(random.randint(1, 10))
        print(f"El hilo {self.name} ha terminado de usar el objeto {num}")

        with Lista.cond:
            Lista.lista[num] = False
            Lista.cond.notify_all()

if __name__ == '__main__':
    for i in range(1, 10):
        objeto = Lista(f"Listado {i}")
        objeto.start()
        objeto.join()
        time.sleep(random.randint(1, 3))