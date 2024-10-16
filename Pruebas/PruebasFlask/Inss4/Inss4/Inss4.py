
#coding: latin1
from pip._vendor import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)
print(response.json())

title = input("Inserta un titulo: ")

todo = {"title":title}
response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)