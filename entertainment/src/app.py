from flask import Flask, request
from entertainment.src import datasource, config

app = Flask(__name__)


@app.route("/movies", methods=['POST'])
def movies():
    data = request.get_json()
    movie_title, movie_runtime, movie_rating = datasource.search_movie_by_genre(data['movieGenres'])
    if movie_rating is None:
        movie_rating = "Unbekannt"
    if movie_runtime is None:
        movie_runtime = "Unbekannt"
    return "Heute kann ich dir diesen Film vorschlagen: " + movie_title +\
           "\nRating: " + movie_rating + "\nSpielzeit: " + movie_runtime


@app.route("/series", methods=['POST'])
def series():
    data = request.get_json()
    series_title, series_runtime, series_rating = datasource.search_series_by_genre(data['movieGenres'])
    if series_rating is None:
        series_rating = "Unbekannt"
    if series_runtime is None:
        series_runtime = "Unbekannt"
    return "Heute kann ich dir diese Serie vorschlagen: " + series_title + \
           "\nRating: " + series_rating + "\nDauer der Folgen: " + series_runtime


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)

