import datetime
from bs4 import BeautifulSoup
import requests
import json

class WelcomeSource:
    def __init__(self):
        self.name = "test"
        self.rapla = "https://rapla.dhbw-stuttgart.de/rapla?key=txB1FOi5xd1wUJBWuX8lJhGDUgtMSFmnKLgAG_NVMhBUYcX7OIFJ2of49CgyjVbV"
        self.city = "Stuttgart"
    def get_welcome_briefing(self):
        answer = ""
        return answer

    def get_motivational_quote(self):
        url = "https://motivational-quotes1.p.rapidapi.com/motivation"

        payload = {
            "key1": "value",
            "key2": "value"
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com",
            "X-RapidAPI-Key": "7489d1be68mshccc0e34a5ecd571p150b3cjsn9b9940bc96dd"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        return response.text

    def get_weahter_data(self):
        url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

        querystring = {"q":self.city,"lat":"0","lon":"0","lang":"de","units":"metric"}

        headers = {
            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
            "X-RapidAPI-Key": "7489d1be68mshccc0e34a5ecd571p150b3cjsn9b9940bc96dd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        text = json.loads(response.text)
        return f"Heute wird es im Durchschnitt {str(text['list'][0]['temp']['average'])} Grad"

    def get_rapla_data(self):
        date = "today"
        link = self.rapla

        if date == "today":
            now = datetime.datetime.now()
        elif date == "tomorrow":
            now = datetime.datetime.now() + datetime.timedelta(days=1)
        else:
            # test if the given date is valid
            try:
                now = datetime.datetime.strptime(date, "%d.%m.%y")
            except:

                return "Invalid Format"

        # add date as url params
        link += "&day=" + str(now.day)
        link += "&month=" + str(now.month)
        link += "&year=" + str(now.year)
        link += "&today=Heute"

        # integer representation of the day in the week, where 0 is monday and 6 is sunday
        weekday = now.weekday()

        if weekday > 4:
            # saturday or sunday

            return ("Free")

        # get html content and parse it with bs4
        webpage = requests.get(link)
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
           
            answer += time[1] + ": " + course + person[:-1] + "\n"

        return answer
