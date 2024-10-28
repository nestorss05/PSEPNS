#coding: latin1
import json

from pip._vendor import requests
from models.Articulo import Articulo
from models.Periodista import Periodista


def main():
    login()
    print("Hasta luego")

def login():
    username = input("User: ")
    password = input("Password: ")
    resultado = requests.post(
        "http://localhost:5050/users/login",
        json={"username": username, "password": password},
        headers={"Content-Type": "application/json"}
    )
    if resultado:
        token = resultado.json().get("token")
        print(token)
        programa(token)
    else:
        print("ERROR: nombre de usuario y/o contraseña incorrecta")

def programa(token: str):
    mostrarMenu()
    opc = int(input("Inserta una opcion: "))
    while opc != 0:
        if opc == 1:
            try:
                response = requests.get("http://localhost:5050/periodistas/",
                                        headers={"Authorization": "Bearer " + token})
                if response.status_code == 200:
                    print(response.json())
                else:
                    print("Se ha producido un error")
            except Exception as e:
                print(e)
        else:
            print("WIP")
        mostrarMenu()
        opc = int(input("Inserta una opcion: "))

def mostrarMenu():
    print("API de periodistas y articulos")
    print("0. Salir")
    print("PERIODISTAS")
    print("1. Ver periodistas")
    print("2. Ver periodista")
    print("3. Añadir periodista")
    print("4. Modificar periodista")
    print("5. Eliminar periodista")
    print("ARTICULOS")
    print("6. Ver articulos")
    print("7. Ver articulo")
    print("8. Añadir articulo")
    print("9. Modificar articulo")
    print("10. Eliminar articulo")

if __name__ == "__main__":
    main()