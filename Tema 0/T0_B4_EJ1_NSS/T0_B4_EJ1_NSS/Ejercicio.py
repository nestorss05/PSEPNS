class Animal():
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

    def habla():
        return ""

    def __str__(self):
        frase = "Me llamo " + self.nombre + ", tengo " + self.patas + " patas y sueno asi: " + self.habla()

class Gato(Animal):
    def __init__(self, nombre, patas, animal):
        super().__init__(nombre, patas)
        self.animal = animal

    def habla():
        return "Miau"

    def __str__(self):
        frase = "Soy un gato. " + super().__str__()

class Perro(Animal):
    def __init__(self, nombre, patas, animal):
        super().__init__(nombre, patas)
        self.animal = animal

    def habla():
        return "Guau"

    def __str__(self):
        frase = "Soy un perro. " + super().__str__()