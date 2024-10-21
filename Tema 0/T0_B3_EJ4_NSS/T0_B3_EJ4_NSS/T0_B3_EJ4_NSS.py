from itertools import filterfalse


class Articulo:
    def __init__(self, nombre, precio, cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.cuantosQuedan = cuantosQuedan
        self.iva = 0.21

    def getPVP(self):
        precioFinal = self.precio + (self.precio*self.iva)
        return precioFinal

    def getPVPDescuento(self, descuento):
        precioFinal = self.precio + (self.precio*self.iva) - descuento
        return precioFinal

    def vender(self, cantidad):
        res = False
        if (cantidad <= self.cuantosQuedan):
            self.cuantosQuedan = self.cuantosQuedan - cantidad
            res = True
        return res

    def almacenar(self, cantidad):
        self.cuantosQuedan = self.cuantosQuedan + cantidad

    def __str__(self):
        frase = "Nombre: " + self.nombre + "\n"
        frase += "Precio: " + str(self.precio) + "\n"
        frase += "Stock: " + str(self.cuantosQuedan)

    def __eq__(self, otro):
        iguales = False
        if self.nombre == otro.nombre:
            iguales = True
        return iguales

    def __lt__(self, otro):
        menor = False
        if self.nombre < otro.nombre:
            menor = True
        return menor