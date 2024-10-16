class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular(self, cant):
        res = self.precio * cant
        return res

    def __str__(self):
        msg = "Nombre: " + self.nombre + "\n"
        msg += "Precio: " + str(self.precio)
        return msg

    def __lt__(self, otro):
        menor = False
        if self.precio < otro.precio:
            menor = True
        return menor

class Perecedero(Producto):
    def __init__(self, nombre, precio, diasACaducar):
        super().__init__(nombre, precio)
        self.diasACaducar = diasACaducar
    
    def calcular(self, cant):
        res = super().calcular(cant)
        if self.diasACaducar == 3:
            res = res / 2
        elif self.diasACaducar == 2:
            res = res / 3
        elif self.diasACaducar == 1:
            res = res / 4
        return res

    def __str__(self):
        msg = super().__str__()
        msg += "\nDias a caducar: " + str(self.diasACaducar)
        return msg

class NoPerecedero(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo
    
    def calcular(self, cant):
        res = super().calcular(cant)
        return res

    def __str__(self):
        msg = super().__str__()
        msg += "\nTipo: " + str(self.tipo)
        return msg