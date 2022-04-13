from wsgiref import headers
import requests
import json
import io
from geopy.geocoders import Nominatim
from datetime import timedelta


def __init__(self) -> None:
    self.tkapikey = "9775658e-0a17-f909-9013-dd795e16e340"
    self.home = "Etzelstr."

def get_Gas_Stations_Rad(city, fuel):
    url = "https://creativecommons.tankerkoenig.de/json/list.php?"
    apikey = "9775658e-0a17-f909-9013-dd795e16e340"
    lat, lng  = getCoords(city)
    querystring = {"lat": lat, "lng":lng, "rad":"3", "type":fuel, "sort":"price", "apikey":"9775658e-0a17-f909-9013-dd795e16e340"} 
    headers = {
        "TK-API-Host": "creativecommons.tankerkoenig.de",
        "TK-API-Key": "9775658e-0a17-f909-9013-dd795e16e340"
    }
    data = json.load(io.BytesIO(requests.request("GET", url, headers=headers, params=querystring).content.replace(b"'", b'"')))
    response = "Hier die nächsten Tankstellen in dieser Stadt:"
    if(len(data['stations'])):
        for i in data['stations']:
            response += "\n" + i['name'] + ", " + i['street'] + " " + i['houseNumber'] + "\nPreis: " + str(i['price'])
    else:
        for i in data['stations'][:2]:
            response += "\n" + i['name'] + ", " + i['street'] + " " + i['houseNumber'] + "\nPreis: " + str(i['price'])
    return response

def getCoords(cityname):
    address= cityname
    geolocator = Nominatim(user_agent="Your_Name")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude


def get_weather_data(city):

    url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

    querystring = {"q": city, "lat": "0", "lon": "0", "lang": "de", "units": "metric"}

    headers = {
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
        "X-RapidAPI-Key": "7489d1be68mshccc0e34a5ecd571p150b3cjsn9b9940bc96dd"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    text = json.loads(response.text)   
    if not response.ok:
        return "Kein valider Ort angegeben."

    today = text['list'][0]
    if today['humidity'] > 50:
        humidity = 'niedriger'
    else:
        humidity = 'hoher'

    if today['temp']['average'] < 16:
        clothing = "Du solltest dir eine Jacke anziehen."
    elif today['temp']['average'] < 22:
        clothing = "Du solltest dir noch einen Pulli mitnehmen."
    else:
        clothing = "Heute reicht ein T-Shirt."
    # return f"Heute wird es im Durchschnitt {str(text['list'][0]['temp']['average'])} Grad"
    return f"Heute wird es in {str(text['city']['name'])} im Durchschnitt {str(today['temp']['average'])} Grad mit {humidity} Luftfeuchtigkeit. {clothing}"

def get_Route(origin, destination):
    url = "https://api.mapbox.com/directions/v5/mapbox/driving/"
    accesstoken = "pk.eyJ1IjoiYWxleGhvYmRlbiIsImEiOiJjbDF3czlqaWswbTdmM2ltcDBlemlzMG91In0.IRDjSyBm9HPJvLgypn31bA"

    origin_lat, origin_lng = getCoords(origin)
    destination_lat, destination_lng = getCoords(destination)

    url += str(origin_lng) + "," + str(origin_lat) + ";" + str(destination_lng) + "," + str(destination_lat)

    headers = {
        "MB-API-Host": "https://docs.mapbox.com/",
        "MB-Access-Token": "pk.eyJ1IjoiYWxleGhvYmRlbiIsImEiOiJjbDF3czlqaWswbTdmM2ltcDBlemlzMG91In0.IRDjSyBm9HPJvLgypn31bA"
    }

    querystring = {"geometries": "geojson", "access_token": accesstoken, "steps":"true", "language":"de", "voice_instructions":"true"}

    data = json.load(io.BytesIO(requests.request("GET", url, headers=headers, params=querystring).content.replace(b"'", b'"')))
    response = "Ich habe folgende Route für dich:\n"
    for i in data['routes'][0]['legs'][0]['steps']:
        for j in i['voiceInstructions']:
            response += j['announcement']

    return response

def get_Distance(origin, destination):
    url = "https://api.mapbox.com/directions/v5/mapbox/driving/"
    accesstoken = "pk.eyJ1IjoiYWxleGhvYmRlbiIsImEiOiJjbDF3czlqaWswbTdmM2ltcDBlemlzMG91In0.IRDjSyBm9HPJvLgypn31bA"

    origin_lat, origin_lng = getCoords(origin)
    destination_lat, destination_lng = getCoords(destination)

    url += str(origin_lng) + "," + str(origin_lat) + ";" + str(destination_lng) + "," + str(destination_lat)

    headers = {
        "MB-API-Host": "https://docs.mapbox.com/",
        "MB-Access-Token": "pk.eyJ1IjoiYWxleGhvYmRlbiIsImEiOiJjbDF3czlqaWswbTdmM2ltcDBlemlzMG91In0.IRDjSyBm9HPJvLgypn31bA"
    }

    querystring = {"geometries": "geojson", "access_token": accesstoken, "steps":"true", "language":"de", "voice_instructions":"true"}

    data = json.load(io.BytesIO(requests.request("GET", url, headers=headers, params=querystring).content.replace(b"'", b'"')))

    response = "Dein Ziel ist " + str(timedelta(seconds=(data['routes'][0]['legs'][0]["duration"]))).split(".")[0] + " Stunden und " + str(data['routes'][0]['legs'][0]["distance"]/1000) + " Km entfernt."
    return response

def get_Bahn(self):
    url = "http://api.deutschebahn.com/free1bahnql/v1"