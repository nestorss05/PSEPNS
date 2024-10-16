#coding: latin1
from pip._vendor import requests
api_url = "https://jsonplaceholder.typicode.com/todos"

userID = int(input("Inserta una ID de usuario: "))
title = input("Inserta un titulo: ")
completed = False
completedStr = input("¿Esta insertado? ")
completedStr = completedStr.lower()
if completedStr == "si":
    completed = True

todo = {"userId":userID, "title":title, "completed": completed}
response = requests.post(api_url, json=todo)

print(response.json())
print("Codigo de estado: " + str(response.status_code))