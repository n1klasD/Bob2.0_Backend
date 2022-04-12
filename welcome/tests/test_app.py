
from distutils.log import Log
import pytest
from mock import patch, Mock
from flask import request

from ..src import app as flask_app, weather
from ..src import datasources



def test_good_weather():
    with flask_app.test_client() as c:
        place = "Stuttgart"
        rv = c.post('/wetter', json={
            'weatherLocation': place
        })
        answer = weather()
        assert "Grad" in answer and "Luftfeuchtigkeit" in answer and place in answer

def test_bad_weather():
    with flask_app.test_client() as c:
        place = "Stutttgart"
        rv = c.post('/wetter', json={
            'weatherLocation': place
        })
        answer = weather()
        assert "Kein valider Ort angegeben" in answer
 


"""

def test_news(client):

    with patch("welcome.src.datasources.get_news_data") as patched_news_data:
        patched_news_data.return_value = ""


@pytest.fixture
def patched_requests(monkeypatch):
    # store a reference to the old get method
    old_get = requests.post
    def mocked_post(uri, *args, **kwargs):
        json = dict(
        data = lambda: {'data': {'weatherLocation': 'Stuttgart'}},
        )
        
    # finally, patch Requests.get with patched version
    monkeypatch.setattr(requests, 'post', mocked_post)
"""