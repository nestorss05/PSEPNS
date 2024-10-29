from pip._vendor import requests
from models.Articulo import Articulo

def verArticulos():
    response = requests.get("http://localhost:5050/articulos/")
    if response.status_code == 200:
        for articulo in response.json():
            neoarticulo = Articulo(
                id=articulo['id'],
                idPeriodista=articulo['idPeriodista'],
                titulo=articulo['Titulo'],
                cuerpo=articulo['Cuerpo'],
                fecha=articulo['Fecha']
            )
            print(neoarticulo)
    else:
        print("Se ha producido un error")

def verUnArticulo():
    idf = int(input("Inserta el ID del articulo: "))
    response = requests.get("http://localhost:5050/articulos/" + str(idf))
    if response.status_code == 200:
        articulo = response.json()
        neoarticulo = Articulo(
            id=articulo['id'],
            idPeriodista=articulo['idPeriodista'],
            titulo=articulo['Titulo'],
            cuerpo=articulo['Cuerpo'],
            fecha=articulo['Fecha']
        )
        print(neoarticulo)
    else:
        print("Se ha producido un error")

def añadirArticulo(token: str):
    idPeriodista = int(input("Inserta el ID del periodista que ha escrito este articulo: "))
    titulo = input("Inserta el titulo del articulo: ")
    cuerpo = input("Inserta el cuerpo del articulo: ")
    fecha = input("Inserta la fecha del articulo: ")
    datosJSON = {
        "idPeriodista": idPeriodista,
        "Titulo": titulo,
        "Cuerpo": cuerpo,
        "Fecha": fecha
    }
    response = requests.post("http://localhost:5050/articulos/",headers={"Authorization": "Bearer " + token}, json = datosJSON)
    if response.status_code == 201:
        print("Se ha insertado el articulo correctamente")
    else:
        print("Se ha producido un error")

def modificarArticulo(token: str):
    idf = int(input("Inserta el ID del articulo: "))
    response = requests.get("http://localhost:5050/articulos/" + str(idf))
    if response.status_code == 200:

        print("1. Modificar todos los datos (predeterminado)")
        print("2. Modificar un dato (cuerpo)")
        opc = int(input("Elige una opcion: "))

        if opc == 2:
            cuerpo = input("Inserta el cuerpo del articulo: ")
            datosJSON = {
                "Cuerpo": cuerpo,
            }
            response = requests.patch("http://localhost:5050/articulos/" + str(idf),
                                      headers={"Authorization": "Bearer " + token},
                                      json=datosJSON)
            if response.status_code == 200:
                print("Se ha modificado el articulo correctamente")
            else:
                print("Se ha producido un error")
        else:
            idPeriodista = int(input("Inserta el ID del periodista que ha escrito este articulo: "))
            titulo = input("Inserta el titulo del articulo: ")
            cuerpo = input("Inserta el cuerpo del articulo: ")
            fecha = input("Inserta la fecha del articulo: ")
            datosJSON = {
                "idPeriodista": idPeriodista,
                "Titulo": titulo,
                "Cuerpo": cuerpo,
                "Fecha": fecha
            }
            response = requests.put("http://localhost:5050/articulos/" + str(idf),
                                    headers={"Authorization": "Bearer " + token},
                                    json=datosJSON)
            if response.status_code == 200:
                print("Se ha modificado el articulo correctamente")
            else:
                print("Se ha producido un error")

    else:
        print("ERROR: Articulo no encontrado")

def eliminarArticulo(token: str):
    idf = int(input("Inserta el ID del articulo: "))
    response = requests.delete("http://localhost:5050/articulos/" + str(idf),headers={"Authorization": "Bearer " + token})
    if response.status_code == 200:
        print("Se ha eliminado el articulo correctamente")
    else:
        print("Se ha producido un error")