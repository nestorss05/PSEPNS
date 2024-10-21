import json

import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from app.articulos.routes import escribeFichero
from app.periodistas.routes import leeFichero

ficheroUsers = "app/users/data.json"
usersBP = Blueprint('users', __name__)
usersBP.post('/')

def leeFichero():
    archivo = open(ficheroUsers, "r")
    dato = json.load(archivo)
    archivo.close()
    return dato

def escribeFichero(datos):
    archivo = open(ficheroUsers, "w")
    json.dump(datos, archivo)
    archivo.close()

@usersBP.get('/')
def loginUser():
    users = leeFichero()
    if request.is_json:
        user = request.get_json()
        username = user['username']
        password = user['password'].encode('utf-8')
        for userFile in users:
            if userFile['username'] == username:
                passwordFile = userFile['password']
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=username)
                    return {'token': token}, 200
                else:
                    return {'error': 'Incorrect username or password'}, 401
        return {'error': 'User not found'}, 404
    return {"error": "Request must be JSON"}, 415

@usersBP.post('/')
def registerUser():
    users = leeFichero()
    if request.is_json:
        user = request.get_json()
        password = user['password'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashPassword = bcrypt.hashpw(password, salt).hex()
        user['password'] = hashPassword
        users.append(user)
        escribeFichero(users)
        token = create_access_token(identity=user['username'])
        return {'token': token}, 201