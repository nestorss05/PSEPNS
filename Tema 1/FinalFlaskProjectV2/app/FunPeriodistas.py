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

def añadirPeriodista(token: str):
    nombre = input("Inserta el nombre del periodista: ")
    apellidos = input("Inserta los apellidos del periodista: ")
    especialidad = input("Inserta la especialidad del periodista: ")
    dni = input("Inserta el DNI del periodista: ")
    telefono = int(input("Inserta el telefono del periodista: "))
    datosJSON = {
        "Nombre": nombre,
        "Apellidos": apellidos,
        "Especialidad": especialidad,
        "Telefono": telefono,
        "dni": dni
    }
    response = requests.post("http://localhost:5050/periodistas/",headers={"Authorization": "Bearer " + token}, json = datosJSON)
    if response.status_code == 201:
        print("Se ha insertado el periodista correctamente")
    else:
        print("Se ha producido un error")

def modificarPeriodista(token: str):
    idf = int(input("Inserta el ID del periodista: "))
    response = requests.get("http://localhost:5050/periodistas/" + str(idf))
    if response.status_code == 200:

        print("1. Modificar todos los datos (predeterminado)")
        print("2. Modificar un dato (especialidad)")
        opc = int(input("Elige una opcion: "))

        if opc == 2:
            especialidad = input("Inserta la especialidad del periodista: ")
            datosJSON = {
                "Especialidad": especialidad,
            }
            response = requests.patch("http://localhost:5050/periodistas/" + str(idf),
                                      headers={"Authorization": "Bearer " + token},
                                      json=datosJSON)
            if response.status_code == 200:
                print("Se ha modificado el periodista correctamente")
            else:
                print("Se ha producido un error")
        else:
            nombre = input("Inserta el nombre del periodista: ")
            apellidos = input("Inserta los apellidos del periodista: ")
            especialidad = input("Inserta la especialidad del periodista: ")
            dni = input("Inserta el DNI del periodista: ")
            telefono = int(input("Inserta el telefono del periodista: "))
            datosJSON = {
                "Nombre": nombre,
                "Apellidos": apellidos,
                "Especialidad": especialidad,
                "Telefono": telefono,
                "dni": dni
            }
            response = requests.put("http://localhost:5050/periodistas/" + str(idf),
                                    headers={"Authorization": "Bearer " + token},
                                    json=datosJSON)
            if response.status_code == 200:
                print("Se ha modificado el periodista correctamente")
            else:
                print("Se ha producido un error")

    else:
        print("ERROR: Periodista no encontrado")

def eliminarPeriodista(token: str):
    idf = int(input("Inserta el ID del periodista: "))
    response = requests.delete("http://localhost:5050/periodistas/" + str(idf),headers={"Authorization": "Bearer " + token})
    if response.status_code == 200:
        print("Se ha eliminado el periodista correctamente")
    else:
        print("Se ha producido un error")