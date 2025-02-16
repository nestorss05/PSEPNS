import random
import time
from threading import Thread, Event, Barrier, Lock

PERSONAS = 5

class Sala(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.codigo = 1295
        self.adivino = Event()
        self.barrier = Barrier(PERSONAS)
        self.lock = Lock()
        self.pos = 0

    def comprobar_sala(self, numero, nombre):
        res = numero == self.codigo
        if res:
            print(f"({nombre}) Acertado (intento = {numero})")
            self.adivino.set()
        else:
            print(f"({nombre}) No acertado (intento = {numero})")
        return res

    def obtener_posicion(self):
        with self.lock:
            self.pos += 1
            return self.pos

class Persona(Thread):
    def __init__(self, nombre, sala):
        Thread.__init__(self, name=nombre)
        self.sala = sala

    def run(self):
        print(f"({self.name}) Investigando clave...")
        while not self.sala.adivino.is_set():
            clave = random.randint(0, 9999)
            if self.sala.comprobar_sala(clave, self.name):
                break
            time.sleep(1)

        pos = self.sala.obtener_posicion()
        print(f"({self.name}) Esperando a los demas para salir... ({pos}/{PERSONAS})")
        self.sala.barrier.wait()
        print(f"({self.name}) VICTORIA!!!")

if __name__ == '__main__':
    print("EL BESTO ESCAPE ROOM (adivina el numero de 10k combis)")
    sala = Sala()
    threads = []

    for i in range(PERSONAS):
        p = Persona(str(i+1), sala)
        threads.append(p)
        p.start()

    for t in threads:
        t.join()