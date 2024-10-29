from pip._vendor import requests
from models.Periodista import Periodista

def verPeriodistas():
    response = requests.get("http://localhost:5050/periodistas/")
    if response.status_code == 200:
        for periodista in response.json():
            neoperiodista = Periodista(
                id=periodista['id'],
                nombre=periodista['Nombre'],
                apellidos=periodista['Apellidos'],
                especialidad=periodista['Especialidad'],
                telefono=periodista['Telefono'],
                dni=periodista['dni']
            )
            print(neoperiodista)
    else:
        print("Se ha producido un error")

def verUnPeriodista():
    idf = int(input("Inserta el ID del periodista: "))
    response = requests.get("http://localhost:5050/periodistas/" + str(idf))
    if response.status_code == 200:
        periodista = response.json()
        neoperiodista = Periodista(
            id=periodista['id'],
            nombre=periodista['Nombre'],
            apellidos=periodista['Apellidos'],
            especialidad=periodista['Especialidad'],
            telefono=periodista['Telefono'],
            dni=periodista['dni']
        )
        print(neoperiodista)
    else:
        print("Se ha producido un error")