from flask import Flask, request
from entertainment.src import datasource, config

app = Flask(__name__)

@app.route("/movies")
def movies():

    return "Hello from Entertainment dialog"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

