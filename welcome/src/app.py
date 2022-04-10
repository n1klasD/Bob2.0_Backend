from flask import Flask, request
from .datasources import get_weahter_data,get_motivational_quote,get_news,get_todos,get_rapla_data

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

    return f"Guten Morgen {data[userName]}. \
        {get_weahter_data(data[city])} \
        Dein erster Termin ist um 9 Uhr, gefolgt von 13 Uhr danach eine Pause bis 17 Uhr, danach sind deine geplanten Termine erledigt. \
        Was du vielleicht verpasst hast: {get_news(data[news])}.\
        Und vergiss nicht: {get_motivational_quote()}."


@app.route('/wetter', methods=["POST"])
def weather():
    data = request.get_json()

    weather = get_weahter_data(data[city])
    return weather


@app.route('/todo', methods=["POST"])
def todo():
    data = request.get_json()

    return "Heute hast du keine Termine."


@app.route('/termine', methods=["POST"])
def calendar():
    data = request.get_json()

    return "Heute hast du keine Termine."


@app.route('/stundenplan', methods=["POST"])
def timetable():
    data = request.get_json()
    answer = get_rapla_data("txB1FOi5xd1wUJBWuX8lJhGDUgtMSFmnKLgAG_NVMhBUYcX7OIFJ2of49CgyjVbV")
    return answer

