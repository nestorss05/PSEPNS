#coding: latin1
from pip._vendor import requests
salir = False

api_url = "https://jsonplaceholder.typicode.com/todos/"

while (salir is False):
    opcion=int(input("Elige el dato, 1-10 o 0 para salir: "))
    if opcion>0:
        response = requests.get(api_url+str(opcion))
        print(response.json())
    elif opcion<0:
        print("ERROR: opcion invalida")
    else:
        salir = True

print("Hasta pronto")