import datetime
from bs4 import BeautifulSoup
import requests
import json
import os
from dotenv import load_dotenv
import random
import time

def get_API_Key(key):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    load_dotenv(os.path.join(BASEDIR, '.env'))

    return os.getenv(key)


def get_news_data(category,all_news=False):

    url = "https://free-news.p.rapidapi.com/v1/search"
    headers = {
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': get_API_Key('RAPID_KEY')
        }

    if not all_news:
        category = random.choice(category)
        querystring = {"q":category,"lang":"de"}


        response = requests.request("GET", url, headers=headers, params=querystring)
        text = json.loads(response.text)
    
        if not response.ok:
            return (f"{category}: Keine Neuigkeiten.")
        elif not 'articles' in text:
            return (f"{category}: Keine Neuigkeiten.")
        text = text['articles'][0]
        return(f"{category}: {text['title']} ({text['author']}).")
    
    if all_news:
        answer = "Hier sind die heutigen News: \n"
        for cat in category:
            time.sleep(1)
            querystring = {"q":cat,"lang":"de"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            text = json.loads(response.text)
        
            if not response.ok:
                answer += f"{cat}: Keine Neuigkeiten.\n"
                continue
            elif not 'articles' in text:
                answer += f"{cat}: Keine Neuigkeiten.\n"
                continue
            text = text['articles'][0]
            if text['author'] is None:
                text['author'] = "Unbekannt"
            answer += f"{cat}: {text['title']} ({text['author']}).\n"
        return answer
    else:
        return "Es ist etwas schiefgelaufen."

    
def get_motivational_quote():
    
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"
    
    payload = {
        "key1": "value",
        "key2": "value"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com",
        "X-RapidAPI-Key": get_API_Key('RAPID_KEY')
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if not response.ok:
        return ""
    return response.text.replace("\n", "")


def get_weather_data(city):

    url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

    querystring = {"q": city, "lat": "0", "lon": "0", "lang": "de", "units": "metric"}

    headers = {
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
        "X-RapidAPI-Key": get_API_Key('RAPID_KEY')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    text = json.loads(response.text)   
    if not response.ok:
        return "Kein valider Ort angegeben."

    today = text['list'][0]
    if today['humidity'] > 50:
        humidity = 'niedriger'
    else:
        humidity = 'hoher'

    if today['temp']['average'] < 16:
        clothing = "Du solltest dir eine Jacke anziehen."
    elif today['temp']['average'] < 22:
        clothing = "Du solltest dir noch einen Pulli mitnehmen."
    else:
        clothing = "Heute reicht ein T-Shirt."
    # return f"Heute wird es im Durchschnitt {str(text['list'][0]['temp']['average'])} Grad"
    return f"Heute wird es in {str(text['city']['name'])} im Durchschnitt {str(today['temp']['average'])} Grad mit {humidity} Luftfeuchtigkeit. {clothing}"


def get_rapla_data(key):
    rapla = "https://rapla.dhbw-stuttgart.de/rapla?key="
    date = "today"
    link = key

    if date == "today":
        now = datetime.datetime.now()
    elif date == "tomorrow":
        now = datetime.datetime.now() + datetime.timedelta(days=1)
    else:
        # test if the given date is valid
        try:
            now = datetime.datetime.strptime(date, "%d.%m.%y")
        except:

            return "Kein Valides Link Format."

    # add date as url params
    link += "&day=" + str(now.day)
    link += "&month=" + str(now.month)
    link += "&year=" + str(now.year)
    link += "&today=Heute"

    # integer representation of the day in the week, where 0 is monday and 6 is sunday
    weekday = now.weekday()
    if weekday > 4:
        # saturday or sunday

        return ("Heute hast du keine Vorlesungen.")

    # get html content and parse it with bs4
    webpage = requests.get(link,headers={'User-Agent' : 'Mozilla/5.0'})
    
    soup = BeautifulSoup(webpage.text, "html.parser")
    
    answer = "Heute hast du diese Vorlesungen: "

    weekdays_german = ("Mo", "Di", "Mi", "Do", "Fr")

    week_blocks = soup.find_all("td", class_="week_block")
    for week_block in week_blocks:
        
        # get all days plan in matching week and iterte until the right one is found
        info = week_block.a.get_text().split("\n")
        time = info[1].split(" ")
        if weekdays_german.index(time[0]) != weekday:
            continue
        
        course = info[3]
        person = ""
        if "Personen:" in info:
            person += " bei " + info[info.index("Personen:") + 1]

        answer += time[2][:11] + " : " + course + person[:-1] + ". "
    if answer == "Heute hast du diese Vorlesungen: ":
        return "Heute hast du keine Vorlesungen."
    return answer