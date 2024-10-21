#coding: latin1
from pip._vendor import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)
print(response.json())

userID = int(input("Inserta una ID de usuario: "))
title = input("Inserta un titulo: ")
completed = False
completedStr = input("¿Esta insertado? ")
completedStr = completedStr.lower()
if completedStr == "si":
    completed = True

todo = {"userId":userID, "title":title, "completed": completed}
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)