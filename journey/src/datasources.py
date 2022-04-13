from wsgiref import headers
import requests
import json
import io
from geopy.geocoders import Nominatim
from datetime import timedelta

class Journeysource:

    def __init__(self) -> None:
        self.tkapikey = "9775658e-0a17-f909-9013-dd795e16e340"
        self.home = "Etzelstr."

    def get_Gas_Stations_Rad(self, city):
        url = "https://creativecommons.tankerkoenig.de/json/list.php?"
        apikey = "9775658e-0a17-f909-9013-dd795e16e340"
        lat, lng  = self.getCoords(city)
        querystring = {"lat": lat, "lng":lng, "rad":"2", "type":"all", "apikey":"9775658e-0a17-f909-9013-dd795e16e340"} 
        headers = {
            "TK-API-Host": "creativecommons.tankerkoenig.de",
            "TK-API-Key": "9775658e-0a17-f909-9013-dd795e16e340"
        }
        data = json.load(io.BytesIO(requests.request("GET", url, headers=headers, params=querystring).content.replace(b"'", b'"')))
        response = "Hier die nächsten Tankstellen in dieser Stadt:"
        for i in data['stations']:
            response += "\n" + i['name'] + ", " + i['street'] + " " + i['houseNumber']
        return response

    def getCoords(cityname):
        address= cityname
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(address)
        return location.latitude, location.longitude

    def get_weather_data(self):
        url = "https://community-open-weather-map.p.rapidapi.com/climate/month"
        querystring = {"q": self.city, "lat": "0", "lon": "0", "lang": "de", "units": "metric"}
        headers = {
            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
            "X-RapidAPI-Key": "7489d1be68mshccc0e34a5ecd571p150b3cjsn9b9940bc96dd"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        text = json.loads(response.text)
        # return f"Heute wird es im Durchschnitt {str(text['list'][0]['temp']['average'])} Grad"
        return f"Heute wird es im Durchschnitt {str(text)} Grad"

    def get_Route(self, origin, destination):
        url = "https://api.mapbox.com/directions/v5/mapbox/driving/"
        accesstoken = "pk.eyJ1IjoiYWxleGhvYmRlbiIsImEiOiJjbDF3czlqaWswbTdmM2ltcDBlemlzMG91In0.IRDjSyBm9HPJvLgypn31bA"

        origin_lat, origin_lng = self.getCoords(origin)
        destination_lat, destination_lng = self.getCoords(destination)

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
                respone += j['announcement']

        return response

    def get_Distance(self, origin, destination):
        url = "https://api.mapbox.com/directions/v5/mapbox/driving/"
        accesstoken = "pk.eyJ1IjoiYWxleGhvYmRlbiIsImEiOiJjbDF3czlqaWswbTdmM2ltcDBlemlzMG91In0.IRDjSyBm9HPJvLgypn31bA"

        origin_lat, origin_lng = self.getCoords(origin)
        destination_lat, destination_lng = self.getCoords(destination)

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