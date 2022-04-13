#from crypt import methods
from flask import Flask, request
from . import datasources

app = Flask(__name__)

home = "homeLocation"
work = "workingLocation"
fuel = "gasolineType"

@app.route('/')
def index():
    return "Hello from journey dialog"

@app.route('/gasStations', methods=["POST"])
def gasStations():
    data = request.get_json()
    if(data[fuel] == "Benzin"):
        data[fuel] = "e5"
    stations = datasources.get_Gas_Stations_Rad(data[home], data[fuel])
    return stations

@app.route('/distance', methods=["POST"])
def getdistance():
    data = request.get_json()
    distances = datasources.get_Distance(data[home], data[work])
    return distances

@app.route('/route', methods=["POST"])
def get_Route():
    data = request.get_json()
    weather = datasources.get_weather_data(data[home])
    route = datasources.get_Route(data[home], data[work])
    return weather + "\n" + route