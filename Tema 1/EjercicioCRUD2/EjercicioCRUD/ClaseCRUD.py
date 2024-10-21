#coding: latin1
from pip._vendor import requests

## opc3: Opciones de modificado
opc3 = int

## Url y contenido de la API
api_url = "https://jsonplaceholder.typicode.com/todos/1"
api_url2 = "https://jsonplaceholder.typicode.com/todos/1" ## Esta se supone que deberia ser una URL alternativa para los articulos, pero por ahora sera la misma URL
todo = ""

## Variables de periodista
idP = int
dni = ""
nombre = ""
apellidos = ""
telefono = int
especialidad = ""

## Variables de articulo
idA = int
titulo = ""
cuerpo = ""
fecha = ""

## Opc2 = 1: creacion de un periodista
def creaPeriodista():
    idP = int(input("Inserta el ID del periodista: "))
    dni = input("Inserta el DNI del periodista: ")
    nombre = input("Inserta el nombre del periodista: ")
    apellidos = input("Inserta los apellidos del periodista: ")
    telefono = int(input("Inserta el telefono del periodista: "))
    especialidad = input("Inserta la especialidad del periodista: ")
    todo = {"id": idP, "dni": dni, "nombre": nombre, "apellidos": apellidos, "telefono": telefono, "especialidad": especialidad}
    response = requests.post(api_url, json=todo)
    print(response.json())
    print("Codigo de estado: " + str(response.status_code))

## Opc2 = 2: modificacion de datos
def modificarPeriodistas():
    opc3 = int(input("¿Telefono (1, predeterminado) / Especialidad? (2): "))

    ## Opc3 = 1: modificacion de telefono
    if opc3 == 2:
        especialidad = input("Inserta la especialidad del periodista: ")
        todo = {"especialidad": especialidad}
                   
    ## Otro: modificacion de especialidad
    else:
        telefono = int(input("Inserta el telefono del periodista: "))
        todo = {"telefono": telefono}

    ## Modificacion de datos
    response = requests.patch(api_url, json=todo)
    print(response.json())
    print("Codigo de estado: " + str(response.status_code))

## Opc2 = 3: muestra de periodistas
def mostrarPeriodistas():
    response = requests.get(api_url)
    print(response.json())

## Opc2 = 4: borrado de periodistas
def borrarPeriodistas():
    idP = int(input("Inserta el ID del periodista: "))
    api_url3 = api_url + "/" + idP
    response = requests.delete(api_url3)
    print("Codigo de estado: " + str(response.status_code))
    print(response.json())

## Articulos

## Opc2 = 1: creacion de un articulos
def crearArticulo():
    idA = int(input("Inserta el ID del articulo: "))
    titulo = input("Inserta el titulo del articulo: ")
    cuerpo = input("Inserta el cuerpo del articulo: ")
    fecha = input("Inserta la fecha del articulo: ")
    idP = int(input("Inserta el ID del periodista: "))
    todo = {"id": idA, "titulo": titulo, "cuerpo": cuerpo, "fecha": fecha, "idPeriodista": idP}
    response = requests.post(api_url2, json=todo)
    print(response.json())
    print("Codigo de estado: " + str(response.status_code))

## Opc2 = 2: modificacion de datos
def modificarArticulos():
    opc3 = int(input("¿Titulo (1, predeterminado) / Cuerpo? (2): "))

    ## Opc3 = 1: modificacion de cuerpo
    if opc3 == 2:
        cuerpo = input("Inserta el cuerpo del articulo: ")
        todo = {"cuerpo": cuerpo}

    ## Otro: modificacion de titulo
    else:
        titulo = input("Inserta el titulo del articulo: ")
        todo = {"titulo": titulo}

    ## Modificacion de datos
    response = requests.patch(api_url2, json=todo)
    print(response.json())
    print("Codigo de estado: " + str(response.status_code))

## Opc2 = 3: muestra de articulos
def mostrarArticulos():
    response = requests.get(api_url2)
    print(response.json())

## Opc2 = 4: borrado de articulos
def borrarArticulos():
    idA = int(input("Inserta el ID del articulo: "))
    api_url3 = api_url2 + "/" + idA
    response = requests.delete(api_url3)
    print("Codigo de estado: " + str(response.status_code))
    print(response.json())