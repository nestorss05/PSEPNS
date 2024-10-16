class Empleado():

    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def __str__(self):
        msg = "Empleado " + self.nombre
        return msg

class Operario(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        msg = super().__str__() + " -> Operario"
        return msg

class Directivo(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        msg = super().__str__() + " -> Directivo"
        return msg

class Oficial(Operario):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        msg = super().__str__() + " -> Oficial"
        return msg

class Tecnico(Operario):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        msg = super().__str__() + " -> Tecnico"
        return msg