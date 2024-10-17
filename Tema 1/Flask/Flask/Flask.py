#coding: latin1
from pip._vendor import requests
from flask import Flask

app = Flask(__name__)

countries = [
        {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
        {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
        {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}
    ]

@app.route('/')
def index():
    return 'XD'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)