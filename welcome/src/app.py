from flask import Flask, request
from .datasources import get_weather_data, get_motivational_quote, get_news_data, get_rapla_data


app = Flask(__name__)

userName = "userName"
rapla = "raplaLink"
city = "weatherLocation"
news = "newsCategories"


@app.route('/')
def index():
    return "Dies ist der Welcome Dialog"


@app.route('/welcome', methods=["POST"])
def briefing():
    data = request.get_json()
    weather = get_weather_data(data[city])
    if not rapla in data:
        stundenplan = ""
    else:
        stundenplan = get_rapla_data(data[rapla])
    if(not "Grad" in weather):
        weather = ""
    
    return f"Guten Morgen {data[userName]}.\
    {weather}\
    {stundenplan}\
    Was du vielleicht verpasst hast: {get_news_data(data[news])}\
    Und vergiss nicht: {get_motivational_quote()}"


@app.route('/wetter', methods=["POST"])
def weather():
    data = request.get_json()
    weather = get_weather_data(data[city])
    return weather

@app.route('/termine', methods=["POST"])
def calendar():
    data = request.get_json()

    return "Heute hast du keine Termine."


@app.route('/stundenplan', methods=["POST"])
def timetable():
    data = request.get_json()
    if not rapla in data:
        return "Kein Stundenplan gesetzt."
    answer = get_rapla_data(data[rapla])
    return answer
