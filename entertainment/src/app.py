from flask import Flask, request
from .datasource import search_movie_by_genre, search_series_by_genre, get_future_race, \
    get_future_football_match_by_team, get_joke
from datetime import date

app = Flask(__name__)


@app.route('/briefing', methods=['POST'])
def briefing():
    data = request.get_json()
    favourite_team, next_match_date, next_match_time, opposing_team = \
        get_future_football_match_by_team(data['footballClub'])
    split_date = next_match_date.split(".")
    day, month, year = int(split_date[0]), int(split_date[1]), int(split_date[2])
    current_date = date.today()
    current_day, current_month, current_year = current_date.day, current_date.month, current_date.year
    if day > current_day and day - current_day <= 1 and month >= current_month and year >= current_year:
        return favourite_team + " spielt am " + next_match_date + " um " + next_match_time + " Uhr gegen " + \
            opposing_team + "."
    race_name, circuit_name, race_date, race_time = get_future_race(next_year=False)
    split_date = race_date.split(".")
    day, month, year = int(split_date[0]), int(split_date[1]), int(split_date[2])
    if day > current_day and day - current_day <= 1 and month >= current_month and year >= current_year:
        return "Als nächstes findet der " + race_name + " (" + circuit_name + ") am " + race_date + " um " + \
               race_time + " Uhr statt."
    movie_title, movie_runtime, movie_rating = search_movie_by_genre(data['movieGenres'])
    return "Heute kann ich dir diesen Film vorschlagen: " + movie_title + \
           "\nRating: " + movie_rating + "\nSpielzeit: " + movie_runtime


@app.route("/movies", methods=['POST'])
def movies():
    data = request.get_json()
    movie_title, movie_runtime, movie_rating = search_movie_by_genre(data['movieGenres'])
    if movie_rating is None:
        movie_rating = "Unbekannt"
    if movie_runtime is None:
        movie_runtime = "Unbekannt"
    if movie_title is None:
        return "Ich habe leider keinen Film gefunden, der deinen Präferenzen entspricht"
    return "Heute kann ich dir diesen Film vorschlagen: " + movie_title + \
        "\nRating: " + movie_rating + "\nSpielzeit: " + movie_runtime


@app.route("/series", methods=['POST'])
def series():
    data = request.get_json()
    series_title, series_runtime, series_rating = search_series_by_genre(data['movieGenres'])
    if series_rating is None:
        series_rating = "Unbekannt"
    if series_runtime is None:
        series_runtime = "Unbekannt"
    if series_title is None:
        return "Ich habe leider keine Serie gefunden, die deinen Präferenzen entspricht"
    return "Heute kann ich dir diese Serie vorschlagen: " + series_title + \
           "\nRating: " + series_rating + "\nDauer der Folgen: " + series_runtime


@app.route("/football", methods=['POST'])
def matches():
    data = request.get_json()
    favourite_team, next_match_date, next_match_time, opposing_team = \
        get_future_football_match_by_team(data['footballClub'])
    if favourite_team == next_match_time == next_match_time == opposing_team == -1:
        return "Für " + data['footballClub'] + " wurden leider keine geplanten Spiele gefunden."
    return favourite_team + " spielt am " + next_match_date + " um " + next_match_time + " Uhr gegen " + \
        opposing_team + "."


@app.route("/formulaOne", methods=['POST'])
def races():
    data = request.get_json()
    race_name, circuit_name, race_date, race_time = get_future_race(next_year=False)
    return "Als nächstes findet der " + race_name + " (" + circuit_name + ") am " + race_date + " um " + race_time + \
           " Uhr statt."


@app.route("/comedy", methods=['POST'])
def jokes():
    data = request.get_json()
    joke = get_joke()
    if joke != "No joke found":
        return joke
    return "Leider habe ich keinen Witz gefunden."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
