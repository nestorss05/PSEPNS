from flask import *
from flask_jwt_extended import JWTManager
from app.articulos.routes import articulosBP
from app.periodistas.routes import periodistasBP
from app.users.routes import usersBP
import string
import random

## Para generar la contraseña aleatoria, he importado las librerias string y random, y he guardado la contraseña en una variable mediante la funcion random.SystemRandom()

passwd = "".join(
    random.SystemRandom().choice(string.ascii_letters + string.digits)
    for _ in range(8)
)
app = Flask(__name__)
app.config['SECRET_KEY'] = passwd
jwt = JWTManager(app)

app.register_blueprint(periodistasBP, url_prefix='/periodistas')
app.register_blueprint(articulosBP, url_prefix='/articulos')
app.register_blueprint(usersBP, url_prefix='/users')