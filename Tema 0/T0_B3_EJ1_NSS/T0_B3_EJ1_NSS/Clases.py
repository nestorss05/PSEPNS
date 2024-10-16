class CuentaCorriente:
    def __init__(self, dni, saldo):
        self.dni = dni
        self.nombre = ""
        self.saldo = saldo
    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo
    def sacarDinero(self, cant):
        res = False
        if cant <= self.saldo:
            self.saldo = self.saldo - cant
            res = True
        return res
    def ingresarDinero(self, cant):
        self.saldo = self.saldo + cant
    def __str__(self):
        cad = "DNI: " + self.dni + "\n"
        cad += "Nombre: " + self.nombre + "\n"
        cad += "Saldo: " + str(self.saldo)
    def __eq__(self, objeto):
        iguales = False
        if self.dni == objeto.dni:
            iguales = True
        return iguales
    def __lt__(self, objeto):
        menor = False
        if self.saldo < objeto.saldo:
            menor = True
        return menor