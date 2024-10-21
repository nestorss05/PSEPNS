from flask import *
from flask_jwt_extended import JWTManager
from app.articulos.routes import articulosBP
from app.periodistas.routes import periodistasBP
from app.users.routes import usersBP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nestorss'
jwt = JWTManager(app)

app.register_blueprint(periodistasBP, url_prefix='/periodistas')
app.register_blueprint(articulosBP, url_prefix='/articulos')
app.register_blueprint(usersBP, url_prefix='/users')