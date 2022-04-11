from flask import Flask, request
import datasources


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
        {datasources.get_weather_data(data[city])} \
        Dein erster Termin ist um 9 Uhr, gefolgt von 13 Uhr danach eine Pause bis 17 Uhr, danach sind deine geplanten Termine erledigt. \
        Was du vielleicht verpasst hast: {datasources.get_news_data(data[news])}.\
        Und vergiss nicht: {datasources.get_motivational_quote()}."


@app.route('/wetter', methods=["POST"])
def weather():
    data = request.get_json()
    weather = datasources.get_weather_data(data[city])
    return weather

@app.route('/termine', methods=["POST"])
def calendar():
    data = request.get_json()

    return "Heute hast du keine Termine."


@app.route('/stundenplan', methods=["POST"])
def timetable():
    data = request.get_json()
    answer = datasources.get_rapla_data("txB1FOi5xd1wUJBWuX8lJhGDUgtMSFmnKLgAG_NVMhBUYcX7OIFJ2of49CgyjVbV")
    return answer

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)