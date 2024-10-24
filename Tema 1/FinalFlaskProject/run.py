#coding: latin1
from pip._vendor import requests
from app import app
@app.route('/')
def index():
    return 'Tremendo proyecto Flask veo aqui. Una pena que esta no sea la manera de acceder a el...'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)