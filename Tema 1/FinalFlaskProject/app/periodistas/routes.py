from flask import *

periodistasBP = Blueprint('periodistas', __name__)

def leeFichero():
    archivo = open("database.json", "r")
    periodistas = json.load(archivo)
    archivo.close()
    return periodistas

def escribeFichero(periodistas):
    archivo = open("database.json", "w")
    json.dump(periodistas, archivo)
    archivo.close()

@periodistasBP.get("/")
def get_periodistas():
    periodistas = leeFichero()
    return jsonify(periodistas)

@periodistasBP.get("/<int:id>")
def get_periodista(id):
    periodistas = leeFichero()
    for periodista in periodistas:
        if periodista['id'] == id:
            return periodista, 200
    return {"error": "Periodista no encontrado"}, 404

def _find_next_id():
    periodistas = leeFichero()
    return max(periodista["id"] for periodista in periodistas) + 1

@periodistasBP.post("/")
def add_periodista():
    periodistas = leeFichero()
    if request.is_json:
        periodista = request.get_json()
        periodista["id"] = _find_next_id()
        periodistas.append(periodista)
        escribeFichero(periodistas)
        return periodista, 201
    return {"error": "La peticion debe ser JSON"}, 415

@periodistasBP.put("/<int:id>")
@periodistasBP.patch("/<int:id>")
def modify_periodista(id):
    periodistas = leeFichero()
    if request.is_json:
        newPeriodista = request.get_json()
        for periodista in periodistas:
            if periodista["id"] == id:
                for element in newPeriodista:
                    periodista[element] = newPeriodista[element]
                    escribeFichero(periodistas)
                return periodista, 200
    return {"error": "La peticion debe ser JSON"}, 415

@periodistasBP.delete("/<int:id>")
def delete_periodista(id):
    periodistas = leeFichero()
    for periodista in periodistas:
        if periodista["id"] == id:
            periodistas.remove(periodista)
            escribeFichero(periodistas)
            return "{}", 200
    return {"error": "Periodista no encontrado"}, 404