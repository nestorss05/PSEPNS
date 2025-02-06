import random
from threading import Condition, Thread

INTENTOS = 10
Acertado = False

class Numero:
    def __init__(self):
        self.numero = random.randint(0, 100)
        self.cond = Condition()

    def adivinar_numero(self, nombre):
        global Acertado
        while not Acertado:
            numero = random.randint(0, 100)

            with self.cond:
                if Acertado:
                    break

                if numero == self.numero:
                    print(f"({nombre}) MIO!!! (numero: {numero})")
                    Acertado = True
                    self.cond.notify_all()
                    break
                else:
                    print(f"({nombre}) No acerte (numero: {numero})")

            random.uniform(0.05, 0.20)

        print(f"({nombre}) Mierda, ya acerto")

class Intentador(Thread):
    def __init__(self, nombre, numero):
        Thread.__init__(self, name=nombre)
        self.numero = numero

    def run(self):
        self.numero.adivinar_numero(self.name)

if __name__ == '__main__':
    numero = Numero()
    hilos = []

    for i in range(INTENTOS):
        intnt = Intentador(str(i+1), numero)
        hilos.append(intnt)
        intnt.start()

    for h in hilos:
        h.join()