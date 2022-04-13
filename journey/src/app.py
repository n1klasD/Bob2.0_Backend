from crypt import methods
from flask import Flask, request
from .datasources import get_Gas_Stations_Rad, get_Distance, get_Route

app = Flask(__name__)

home = "homeLocation"
work = "workingLocation"
sprit = "gasolineType"

@app.route('/')
def index():
    return "Hello from journey dialog"

@app.route('/gasStations', methods=["POST"])
def gasStations():
    data = request.get_json()
    stations = get_Gas_Stations_Rad(data[home])
    return stations

@app.route('/distance', methods=["POST"])
def getdistance():
    data = request.get_json()
    distances = get_Distance(data[home], data[work])
    return distances

@app.router('/route', methods=["POST"])
def get_Route():
    data = request.get_json()
    route = get_Route(data[home], data[work])
    return route