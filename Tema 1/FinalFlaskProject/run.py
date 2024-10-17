#coding: latin1
from pip._vendor import requests
from app import app
@app.route('/')
def index():
    return 'XD'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)