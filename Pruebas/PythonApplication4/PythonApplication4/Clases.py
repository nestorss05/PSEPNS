class Padre():
    def __init__(self, n):
        self.nombre = n

    def saludo(self):
        print("Hola, soy el padre:", self.nombre)

class Hija(Padre):
    def __init__(self, n, padre):
        self.padre = padre
        super().__init__(n)

    def saludo(self):
        print("Hola, soy la hija:", self.nombre, "y mi padre es", self.padre.nombre)