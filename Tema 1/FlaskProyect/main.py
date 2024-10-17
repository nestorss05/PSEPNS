#coding: latin1
from pip._vendor import requests
from flask import *

app = Flask(__name__)

periodistas = [
        {"id": 1, "dni": "23556785F", "Nombre": "Pepitto", "Apellidos": "Sanchez", "Telefono": 111111111, "Especialidad": "Investigacion"},
        {"id": 2, "dni": "77443678R", "Nombre": "Florentino", "Apellidos": "Martinez", "Telefono": 222222222, "Especialidad": "Ambiental"},
        {"id": 3, "dni": "88643357T", "Nombre": "Eusebio", "Apellidos": "Flores", "Telefono": 333333333, "Especialidad": "Turistico"},
    ]

articulos = [
        {"id": 1, "Titulo": "Caen bombas nucleares por el territorio verdirrojo", "Cuerpo": "El presidente de la republica disuelve el gobierno, el pais y establece el estado de guerra", "Fecha": "20/02/2022", "idPeriodista": 1},
        {"id": 2, "Titulo": "Plaza Mayor de Once abarrotada por la victoria republicana", "Cuerpo": "Los verdirrojos celebran la victoria, causando que la plaza mayor quede abarrotada", "Fecha": "1/06/2023", "idPeriodista": 3},
        {"id": 3, "Titulo": "Masivos incendios en las siete torres causan grave deterioro ambiental", "Cuerpo": "El ataque a las siete torres han causado una gran cantidad de contaminacion por toda la ciudad de Once", "Fecha": "2/11/2024", "idPeriodista": 2},
    ]

@app.get("/periodistas")
def get_periodistas():
    return jsonify(periodistas)

@app.get("/periodistas/<int:id>")
def get_periodista(id):
    for periodista in periodistas:
        if periodista['id'] == id:
            return periodista, 200
    return {"error": "Periodista no encontrado"}, 404

def _find_next_id():
    return max(periodista["id"] for periodista in periodistas) + 1

@app.post("/periodistas")
def add_periodista():
    if request.is_json:
        periodista = request.get_json()
        periodista["id"] = _find_next_id()
        periodistas.append(periodista)
        return periodista, 201
    return {"error": "La peticion debe ser JSON"}, 415

@app.put("/periodistas/<int:id>")
@app.patch("/periodistas/<int:id>")
def modify_periodista(id):
    if request.is_json:
        newPeriodista = request.get_json()
        for periodista in periodistas:
            if periodista["id"] == id:
                for element in newPeriodista:
                    periodista[element] = newPeriodista[element]
                return periodista, 200
    return {"error": "La peticion debe ser JSON"}, 415

@app.delete("/periodistas/<int:id>")
def delete_periodista(id):
    for periodista in periodistas:
        if periodista["id"] == id:
            periodistas.remove(periodista)
            return "{}", 200
    return {"error": "Periodista no encontrado"}, 404

## Articulos

@app.get("/articulos")
def get_articulos():
    return jsonify(articulos)

@app.get("/articulos/<int:id>")
def get_articulo(id):
    for articulo in articulos:
        if articulo['id'] == id:
            return articulo, 200
    return {"error": "Articulo no encontrado"}, 404

def _find_next_id():
    return max(articulo["id"] for articulo in articulos) + 1

@app.post("/articulos")
def add_articulo():
    if request.is_json:
        articulo = request.get_json()
        articulo["id"] = _find_next_id()
        articulos.append(articulo)
        return articulo, 201
    return {"error": "La peticion debe ser JSON"}, 415

@app.put("/articulos/<int:id>")
@app.patch("/articulos/<int:id>")
def modify_articulo(id):
    if request.is_json:
        newArticulo = request.get_json()
        for articulo in articulos:
            if articulo["id"] == id:
                for element in newArticulo:
                    articulo[element] = newArticulo[element]
                return articulo, 200
    return {"error": "La peticion debe ser JSON"}, 415

@app.delete("/articulos/<int:id>")
def delete_articulo(id):
    for articulo in articulos:
        if articulo["id"] == id:
            articulos.remove(articulo)
            return "{}", 200
    return {"error": "Articulo no encontrado"}, 404

@app.route('/')
def index():
    return 'XD'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)