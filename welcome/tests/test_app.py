
from distutils.log import Log
import pytest
from mock import patch, Mock
from flask import request

from ..src import app as flask_app, weather,briefing, index
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
 
def test_briefing():
    with flask_app.test_client() as c:
        place = "Stuttgart"
        userName = "Simon"
        rv = c.post('/welcome', json={
            'weatherLocation': place,
            'userName': userName,
            'newsCategories': ["Deutschland"]
        })
        answer = briefing()
        assert place in answer and userName in answer

def test_briefing_no_weather():
    with flask_app.test_client() as c:
        place = "Stutttgart"
        userName = "Simon"
        rv = c.post('/welcome', json={
            'weatherLocation': place,
            'userName': userName,
            'newsCategories': "Deutschland"
        })
        answer = briefing()
        assert place not in answer and userName in answer and "Ort" not in answer
 
def test_index():
    answer = index()
    assert answer == "Dies ist der Welcome Dialog"

def test_news():
    with flask_app.test_client() as c:
        cats = ["Deutschland", "Crypto", "Russland"]
        userName = "Simon"
        place = "Stuttgart"
        rv = c.post('/welcome', json={
            'weatherLocation': place,
            'userName': userName,
            'newsCategories': cats
        })
        answer = briefing()
        assert any(cat in answer for cat in cats)