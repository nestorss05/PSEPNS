class Libro:
    def __init__(self, titulo, autor, nEjemplares, nPrestados):
        self.titulo = titulo
        self.autor = autor
        self.nEjemplares = nEjemplares
        self.nPrestados = nPrestados
    def prestamo(self):
        prestado = False
        if self.nEjemplares >= 1:
            self.nPrestados = self.nPrestados + 1
            self.nEjemplares = self.nEjemplares - 1
            prestado = True
        return prestado
    def devolucion(self):
        devuelto = False
        if self.nPrestados >= 1:
            self.nEjemplares = self.nEjemplares + 1
            self.nPrestados = self.nPrestados - 1
            devuelto = True
        return devuelto
    def __str__(self):
        frase = "Titulo: " + self.titulo + "\n"
        frase += "Autor: " + self.autor + "\n"
        frase += "Nº de ejemplares: " + str(self.nEjemplares) + "\n"
        frase += "Nº prestados: " + str(self.nPrestados)
    def __eq__(self, otro):
        iguales = False
        if self.titulo == otro.titulo & self.autor == otro.autor:
            iguales = True
        return iguales
    def __lt__(self, otro):
        menor = False
        if self.autor < otro.autor:
            menor = True
        return menor