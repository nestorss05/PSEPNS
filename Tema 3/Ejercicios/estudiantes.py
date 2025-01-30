import random
from threading import Thread, Condition
import time

estudiantes = 4
libros = 9

class Biblioteca(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.libros = [True] * libros
        self.cond = Condition()

    def reservar_libros(self, estudiante, libro1, libro2):
        with self.cond:
            while not (self.libros[libro1] and self.libros[libro2]):
                print(f"El estudiante {estudiante} esta esperando a los libros {libro1} y {libro2}")
                self.cond.wait()

            self.libros[libro1] = False
            self.libros[libro2] = False
            print(f"El estudiante {estudiante} ha reservado los libros {libro1} y {libro2}")

    def devolver_libros(self, estudiante, libro1, libro2):
        with self.cond:
            self.libros[libro1] = True
            self.libros[libro2] = True
            print(f"El estudiante {estudiante} ha devuelto los libros {libro1} y {libro2}")
            self.cond.notify_all()

class Estudiante(Thread):
    def __init__(self, biblioteca, num, libro1, libro2):
        Thread.__init__(self, name=str(num))
        self.biblioteca = biblioteca
        self.libro1 = libro1
        self.libro2 = libro2

    def run(self):
        print(f"{self.name} va a la biblioteca")
        time.sleep(random.randint(1, 3))
        self.biblioteca.reservar_libros(self.name, self.libro1, self.libro2)
        print(f"({self.name}) Leyendo los libros {self.libro1} y {self.libro2}...")
        time.sleep(random.randint(3, 10))
        print(f"({self.name}) Libros leidos")
        self.biblioteca.devolver_libros(self.name, self.libro1, self.libro2)

if __name__ == '__main__':
    print("Estudiantes y libros")
    biblioteca = Biblioteca()
    hilos = []

    for i in range(estudiantes):
        libro1, libro2 = random.sample(range(libros), 2)
        e = Estudiante(biblioteca, i, libro1, libro2)
        hilos.append(e)
        e.start()

    for h in hilos:
        h.join()

    print("Listo")