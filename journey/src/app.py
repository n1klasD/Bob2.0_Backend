#from crypt import methods
from flask import Flask, request
from . import datasources

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
    stations = datasources.get_Gas_Stations_Rad(data[home])
    return stations

@app.route('/distance', methods=["POST"])
def getdistance():
    data = request.get_json()
    distances = datasources.get_Distance(data[home], data[work])
    return distances

@app.route('/route', methods=["POST"])
def get_Route():
    data = request.get_json()
    route = datasources.get_Route(data[home], data[work])
    return route