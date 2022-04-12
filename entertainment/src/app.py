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


@app.route("/football", methods=['POST'])
def matches():
    data = request.get_json()
    favourite_team, next_match_date, next_match_time, opposing_team = datasource.get_future_football_matches_by_team(data['footballClub'])
    if favourite_team == next_match_time == next_match_time == opposing_team == -1:
        return "Für " + data['footballClub'] + " wurden leider keine geplanten Spiele gefunden."
    return favourite_team + " spielt am " + next_match_date + " um " + next_match_time + " Uhr gegen " + opposing_team + "."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)

