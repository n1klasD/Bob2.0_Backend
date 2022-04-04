from flask import Flask, request
import datasources


app = Flask(__name__)


@app.route('/')
def index():
    return "Dies ist der Welcome Dialog"


@app.route('/welcome', methods=["POST"])
def briefing():
    data = request.get_json()
    userName = "Simon"
    sources = datasources.WelcomeSource()
    return f"Guten Morgen {userName}. {sources.get_weahter_data()} Dein erster Termin ist um 9 Uhr, gefolgt von 13 Uhr danach eine Pause bis 17 Uhr, danach sind deine geplanten Termine erledigt. Was du vielleicht verpasst hast: _Nachrichten API_. Und vergiss nicht: {sources.get_motivational_quote()}."


@app.route('/wetter', methods=["POST"])
def weather():
    data = request.get_json()
    sources = datasources.WelcomeSource()
    weather = sources.get_weahter_data()
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
    source = datasources.WelcomeSource()
    answer = source.get_rapla_data()
    return answer


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8001, debug=True)
