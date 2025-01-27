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
    def __init__(self, biblioteca, num):
        Thread.__init__(self, name=str(num))
        self.biblioteca = biblioteca

    def run(self):
        print(f"{self.name} va a la biblioteca")
        time.sleep(random.randint(1, 3))
        libro1, libro2 = random.sample(range(libros), 2)

        self.biblioteca.reservar_libros(self.name, libro1, libro2)
        print(f"({self.name}) Leyendo los libros {libro1} y {libro2}...")
        time.sleep(random.randint(3, 10))
        print("Libros leidos")
        self.biblioteca.devolver_libros(self.name, libro1, libro2)

if __name__ == '__main__':
    print("Estudiantes y libros")
    biblioteca = Biblioteca()
    hilos = []

    for i in range(estudiantes):
        e = Estudiante(biblioteca, i)
        hilos.append(e)
        e.start()

    for h in hilos:
        h.join()

    print("Listo")