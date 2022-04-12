from flask import Flask, request
from entertainment.src import datasource, config

app = Flask(__name__)


@app.route("/movies", methods=['POST'])
def movies():
    data = request.get_json()
    movie = datasource.search_movie_by_genre(data['movieGenres'])
    return "Heute kann ich dir diesen Film vorschlagen: " + str(movie)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)

