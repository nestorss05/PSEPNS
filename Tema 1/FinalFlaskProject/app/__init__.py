from flask import *
from .periodistas.routes import periodistasBP
from .articulos.routes import articulosBP

app = Flask(__name__)

app.register_blueprint(periodistasBP, url_prefix='/periodistas')
app.register_blueprint(articulosBP, url_prefix='/articulos')