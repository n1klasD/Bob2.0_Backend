from flask import Flask
import datasources

app = Flask(__name__)


@app.route('/')
def index():
    return "Dies ist der Welcome Dialog"


@app.route('/welcome', methods=["POST"])
def briefing():
    userName = "Max Mustermann"
    return f"Guten Morgen {userName}. Heute steht ein schöner Tag bevor. Dein erster Termin ist um ..., gefolgt von ... danach eine Pause bis ..., danach sind deine geplanten Termine erledigt. Was du vielleicht verpasst hast: _Nachrichten API_. Und vergiss nicht: _motivational quotes API_."


@app.route('/wetter', methods=["POST"])
def weather():
    return "heute ist ein schoener Tag."


@app.route('/todo', methods=["POST"])
def todo():
    return "Heute hast du keine Termine."


@app.route('/termine', methods=["POST"])
def calendar():
    return "Heute hast du keine Termine."


@app.route('/stundenplan', methods=["POST"])
def timetable():
    source = datasources.WelcomeSource()
    answer = source.get_rapla_data()
    return answer


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8001, debug=True)
