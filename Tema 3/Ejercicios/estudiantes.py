import random
from threading import Thread, Condition
import time

estudiantes = 4
libros = 9

class Libros(Thread):
    def __init__(self):
        Thread.__init__(self)

class Estudiantes(Thread):
    def __init__(self):
        Thread.__init__(self)

if __name__ == '__main__':
    print("Estudiantes y libros")
    libros = Libros()

## TODO Terminar