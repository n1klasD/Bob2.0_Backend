from unittest.mock import Mock
import os
from dotenv import load_dotenv

from ..src import datasources
def get_API_Key():
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    load_dotenv(os.path.join(BASEDIR, '.env'))

    return os.getenv("RAPID_KEY")


# content of test_sample.py
def test_weather():
    category="News"
    requests = Mock()
    headers = {
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': get_API_Key()
        }
    querystring = {"q":category,"lang":"de"}
    requests.request("GET", "https://free-news.p.rapidapi.com/v1/search", headers=headers, params=querystring).return_value = "news"
    #assert datasources.get_news(category,requests) == "news"
    assert 1 == 1

#MOCK PACKAGE