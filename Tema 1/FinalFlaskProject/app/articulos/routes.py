from flask import *
from flask_jwt_extended import jwt_required

articulosBP = Blueprint('articulos', __name__)

def leeFichero():
    archivo = open("app/articulos/database.json", "r")
    articulos = json.load(archivo)
    archivo.close()
    return articulos

def escribeFichero(articulos):
    archivo = open("app/articulos/database.json", "w")
    json.dump(articulos, archivo)
    archivo.close()

@articulosBP.get("/")
def get_articulos():
    articulos = leeFichero()
    return articulos

@articulosBP.get("/<int:id>")
def get_articulo(id):
    articulos = leeFichero()
    for articulo in articulos:
        if articulo['id'] == id:
            return articulo, 200
    return {"error": "Articulo no encontrado"}, 404

def _find_next_id():
    articulos = leeFichero()
    return max(articulo["id"] for articulo in articulos) + 1

@articulosBP.post("/")
@jwt_required()
def add_articulo():
    articulos = leeFichero()
    if request.is_json:
        articulo = request.get_json()
        articulo["id"] = _find_next_id()
        articulos.append(articulo)
        escribeFichero(articulos)
        return articulo, 201
    return {"error": "La peticion debe ser JSON"}, 415

@articulosBP.put("/<int:id>")
@articulosBP.patch("/<int:id>")
@jwt_required()
def modify_articulo(id):
    articulos = leeFichero()
    if request.is_json:
        newArticulo = request.get_json()
        for articulo in articulos:
            if articulo["id"] == id:
                for element in newArticulo:
                    articulo[element] = newArticulo[element]
                    escribeFichero(articulos)
                return articulo, 200
    return {"error": "La peticion debe ser JSON"}, 415

@articulosBP.delete("/<int:id>")
@jwt_required()
def delete_articulo(id):
    articulos = leeFichero()
    for articulo in articulos:
        if articulo["id"] == id:
            articulos.remove(articulo)
            escribeFichero(articulos)
            return "{}", 200
    return {"error": "Articulo no encontrado"}, 404
