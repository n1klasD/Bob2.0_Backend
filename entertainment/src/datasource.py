import random
import requests
from datetime import date
import xmltodict
import json

api_key = "k_qhn64207"
x_auth_token = "65065e29253e4f5abdf58266f37ea73c"


def get_metadata(movie_id):
    url = "https://imdb-api.com/API/Title/"+api_key+"/"+movie_id
    response = requests.get(url)
    movie_metadata = response.json()
    return movie_metadata


def search_movie_by_genre(genres: list[str]):
    movies = []
    url = "https://imdb-api.com/API/AdvancedSearch/"+api_key+"/?genres="
    for genre in genres:
        genre = genre.replace("-", "_").lower()
        url = url+genre+","
    response = requests.get(url)
    data = response.json()
    results = data['results']
    for result in results:
        movies.append(result)
    movie_found = False
    while not movie_found:
        random_index = random.randint(0, len(movies) - 1)
        movie = movies[random_index]
        movie_id = movie['id']
        movie_metadata = get_metadata(movie_id)
        if movie_metadata['type'] == "Movie":
            movie_found = True
    movie_title = movie_metadata['title']
    movie_runtime = movie_metadata['runtimeStr']
    movie_rating = movie_metadata['imDbRating']

    return movie_title, movie_runtime, movie_rating


def search_series_by_genre(genres: list[str]):
    series_list = []
    url = "https://imdb-api.com/API/AdvancedSearch/"+api_key+"/?genres="
    for genre in genres:
        genre = genre.replace("-", "_").lower()
        url = url+genre+","
    response = requests.get(url)
    data = response.json()
    results = data['results']
    for result in results:
        series_list.append(result)
    series_found = False
    while not series_found:
        random_index = random.randint(0, len(series_list) - 1)
        series = series_list[random_index]
        series_id = series['id']
        series_metadata = get_metadata(series_id)
        if series_metadata['type'] == "TVSeries":
            series_found = True
    series_title = series_metadata['title']
    series_runtime = series_metadata['runtimeStr']
    series_rating = series_metadata['imDbRating']

    return series_title, series_runtime, series_rating


def get_future_football_match_by_team(favourite_team: str):
    future_matches_list = []
    bundesliga = get_bundesliga()
    bundesliga_teams = bundesliga['teams']
    favourite_team_id = get_team_id(bundesliga_teams, favourite_team)
    if favourite_team_id != -1:
        url = "https://api.football-data.org/v2/teams/"+str(favourite_team_id)+"/matches/"
        headers = {
            'X-Auth-Token': x_auth_token
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        matches = data['matches']
        for match in matches:
            if match['status'] == "SCHEDULED":
                future_matches_list.append(match)
        if len(future_matches_list) > 0:
            next_match = future_matches_list[0]
            next_match_datetime = next_match['utcDate']
            next_match_date, next_match_time = convert_datetime(next_match_datetime)
            next_match_teams = [next_match['homeTeam']['name'], next_match['awayTeam']['name']]
            if next_match_teams[0] == favourite_team:
                opposing_team = next_match_teams[1]
            else:
                opposing_team = next_match_teams[0]
            return favourite_team, next_match_date, next_match_time, opposing_team
        else:
            return -1, -1, -1, -1
    else:
        return -1, -1, -1, -1


def get_team_id(teams_list, team):
    for entry in teams_list:
        if entry['name'] == team:
            return entry['id']
    return -1


def get_bundesliga():
    url = "https://api.football-data.org/v2/competitions/2002/teams"
    headers = {
        'X-Auth-Token': x_auth_token
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def convert_datetime(next_match_datetime):
    split_string = next_match_datetime.split("T")
    date = split_string[0]
    time = split_string[1]
    split_date = date.split("-")
    split_time = time.split(":")
    day, month, year = split_date[2], split_date[1], split_date[0]
    minutes, hours = split_time[1], split_time[0]
    date = day+"."+month+"."+year
    time = hours+":"+minutes
    return date, time


def get_future_race(next_year):
    current_date = date.today()
    current_year = current_date.year
    url = "http://ergast.com/api/f1/"
    if next_year:
        url = url + str(current_year+1)
    else:
        url = url + str(current_year)
    response = requests.get(url)
    data_as_string = json.dumps(xmltodict.parse(response.text))
    data = json.loads(data_as_string)
    races = data['MRData']['RaceTable']['Race']
    for race in races:
        race_date = race['Date']
        race_time = race['Time']
        split_race_date = race_date.split('-')
        split_race_time = race_time.split(':')
        race_day, race_month, race_year = int(split_race_date[2]), int(split_race_date[1]), int(split_race_date[0])
        race_minutes, race_hours = split_race_time[1], split_race_time[0]
        if race_day >= current_date.day and race_month >= current_date.month and race_year >= current_date.year:
            race_name = race['RaceName']
            circuit_name = race['Circuit']['CircuitName']
            race_date = str(race_day)+"."+str(race_month)+"."+str(race_year)
            race_time = race_hours+":"+race_minutes
            return race_name, circuit_name, race_date, race_time
    # in case there isn't another race this year, the data of the first race of the next year is returned
    return get_future_race(next_year)


# Attempt at scraping, option B if nothing else works
'''def search_movie_by_name(movie):
    return 0


def get_movie_names(a_tags):
    movie_names = []
    for tag in a_tags:
        if "/title/tt" in tag.get('href'):
            tag = str(tag)
            if not "<img" in tag and not "<span>" in tag:
                tag = tag.replace('<', '>')
                split_tag = re.split('>', tag)
                movie_name = split_tag[2]
                movie_names.append(movie_name)
    return movie_names


def get_movie_ratings(div_tags):
    movie_ratings = []
    for tag in div_tags:
        tag_string = str(tag)
        split_tag = re.split('>', tag_string)
        if "class" in split_tag[0] and "lister-item-content" in tag.get('class'):
            if "ratings-bar" in tag_string:
                tag = tag_string
                split_tag = tag.split('<div class="ratings-bar">')
                sub_split = split_tag[1].split('<strong>')
                sub_split[1] = sub_split[1].replace('<', '>')
                sub_sub_split = sub_split[1].split('>')
                movie_rating = sub_sub_split[0]
                movie_ratings.append(movie_rating)
            else:
                movie_ratings.append("Unknown")
    return movie_ratings


def get_movie_durations(p_tags):
    movie_durations = []
    for tag in p_tags:
        if "text-muted" in tag.get('class'):
            tag = str(tag)
            if "<span class=\"ghost\">" in tag:
                if "<span class=\"runtime\">" in tag:
                    split_tag = re.split('<span class=\"runtime\">', tag)
                    subsplit = re.split('</span>', split_tag[1])
                    movie_duration = subsplit[0]
                    movie_durations.append(movie_duration)
                else:
                    movie_durations.append("Unknown")

    return movie_durations


def search_movies_by_genre(genre):
    movies = {
        'names': [],
        'ratings': [],
        'durations': [],
    }
    url = "https://www.imdb.com/search/title/?genres=" + genre
    website = requests.get(url)
    results = BeautifulSoup(website.content, 'html.parser')

    a_tags = results.find_all('a')
    p_tags = results.find_all('p')
    div_tags = results.find_all('div')

    movie_names = get_movie_names(a_tags)
    movie_ratings = get_movie_ratings(div_tags)
    movie_durations = get_movie_durations(p_tags)
    for i in range(0, len(movie_names)):
        movies['names'].append(movie_names[i])
        movies['ratings'].append(movie_ratings[i])
        movies['durations'].append(movie_durations[i])
    random_index = random.randint(0, len(movies['names'])-1)
    return "Vorgeschlagener Film: "+movies['names'][random_index]+"\n" \
           "Rating: "+movies['ratings'][random_index]+"\n"+"" \
           "Spielzeit: "+movies['durations'][random_index]


print(search_movies_by_genre("horror"))'''


