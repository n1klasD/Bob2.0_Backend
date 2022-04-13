from flask import Flask, request
from .datasources import get_Distance, get_Gas_Stations_Rad, get_Route, get_weather_data

app = Flask(__name__)

home = "homeLocation"
work = "workingLocation"
fuel = "gasolineType"
vehicle = "preferredVehicle"


@app.route('/')
def index():
    return "Hello from journey dialog"


@app.route('/gasStations', methods=["POST"])
def gasStations():
    data = request.get_json()
    stations = get_Gas_Stations_Rad(data[home], data[fuel])
    return stations


@app.route('/distance', methods=["POST"])
def getdistance():
    data = request.get_json()
    distances = get_Distance(data[home], data[work], data[vehicle])
    return distances


@app.route('/route', methods=["POST"])
def getRoute():
    data = request.get_json()
    weather = get_weather_data(data[home])
    route = get_Route(data[home], data[work], data[vehicle])
    return weather + "\n" + route
