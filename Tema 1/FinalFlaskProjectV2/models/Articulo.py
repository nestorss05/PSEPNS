class Articulo:
    def __init__(self, cuerpo, fecha, titulo, id, idPeriodista):
        self.cuerpo = cuerpo
        self.fecha = fecha
        self.titulo = titulo
        self.id = id
        self.idPeriodista = idPeriodista

    def __str__(self):
        cad = "ID: " + str(self.id) + "\n"
        cad += "ID de Periodista: " + str(self.idPeriodista) + "\n"
        cad += "Cuerpo: " + self.cuerpo + "\n"
        cad += "Fecha: " + self.fecha + "\n"
        cad += "Titulo: " + self.titulo
        return cad

    def serialize(self):
        return {"id": self.id, "idPeriodista": self.idPeriodista, "cuerpo": self.cuerpo, "fecha": self.fecha, "titulo": self.titulo}