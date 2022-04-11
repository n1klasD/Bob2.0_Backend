import random

from bs4 import BeautifulSoup
import requests
import re


def search_movie_by_name(movie):
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


print(search_movies_by_genre("horror"))



# for movie in found_movies['names']:
#    print(movie)
''' for i in range(0, len(search)):
        movie_id = search[i].movieID
        movie_object = ia.get_movie(movie_id)

        if movie_object == search[i]:
            print(movie_object)
            print(search[i])
            print("wtf")
        else:
            print("Hurensohn")
        for movie_genre in search[i]['genres']:
            if movie_genre == genre:
                genre_fitting_movies.append(search[i])
            else:
                print(movie_genre)
    for movie in search:
        movie_id = movie.movieID
        movie_object = ia.get_movie(movie_id)
        for movie_genre in movie_object['genres']:
            if movie_genre == genre:
                genre_fitting_movies.append(movie_object)
            else:
                print(movie_genre)
        #ia.update(movie_object, info=['genres'])
        #if movie_object.genres.lower() == genre.lower():
        #    genre_fitting_movies.append(movie_object)
        #print(movie_object['name'])'''

'''    the_matrix = ia.get_movie('0133093')
    for director in the_matrix['directors']:
        print(director['name'])
    
    print(sorted(the_matrix.keys()))
    
    print(ia.get_movie_infoset())
    
    ia.update(the_matrix, ['technical'])
    print(the_matrix.infoset2keys['technical'])
    print(the_matrix.get('tech'))
    
    
    
    for i in range(10):
        print(search[i]['title'])'''
