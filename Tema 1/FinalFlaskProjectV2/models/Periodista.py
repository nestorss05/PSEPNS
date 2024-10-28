class Periodista:
    def __init__(self, id, nombre, apellidos, especialidad, telefono, dni):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.especialidad = especialidad
        self.telefono = telefono
        self.dni = dni

    def __str__(self):
        cad = "ID: " + str(self.id) + "\n"
        cad += "Nombre: " + self.nombre + "\n"
        cad += "Apellidos: " + self.apellidos + "\n"
        cad += "Especialidad: " + self.especialidad + "\n"
        cad += "Telefono: " + str(self.telefono) + "\n"
        cad += "DNI: " + self.dni + "\n"
        return cad

    def serialize(self):
        return {"id": self.id, "Nombre": self.nombre, "Apellidos": self.apellidos, "Especialidad": self.especialidad, "Telefono": self.telefono, "dni": self.dni}