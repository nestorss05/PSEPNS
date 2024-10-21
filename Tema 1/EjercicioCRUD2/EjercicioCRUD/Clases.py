#coding: latin1
class Periodista:
    def __init__(self, id, dni, nombre, apellidos, telefono, especialidad):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.especialidad = especialidad

class Articulo:
    def __init__(self, id, titulo, cuerpo, fecha, idPeriodista):
        self.id = id
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.fecha = fecha
        self.idPeriodista = idPeriodista