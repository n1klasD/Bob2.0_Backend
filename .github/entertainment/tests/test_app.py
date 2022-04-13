from distutils.log import Log
import pytest
from mock import patch, Mock
from flask import request
import time

from ..src import app as flask_app, movies, series, matches, races
from ..src import datasource


def test_horror_action_movie():
    with flask_app.test_client() as c:
        genres = ["horror", "action"]
        rv = c.post('/movies', json={
            'movieGenres': genres
        })
        answer = movies()
        assert "Rating" in answer and "Spielzeit" in answer


def test_scifi_romance_movie():
    with flask_app.test_client() as c:
        genres = ["sci-fi", "romance"]
        rv = c.post('/movies', json={
            'movieGenres': genres
        })
        answer = movies()
        assert "Rating" in answer and "Spielzeit" in answer


def test_bad_movie():
    with flask_app.test_client() as c:
        genres = ["lkjdddwlkjwdajkldwalkawldkwl", "oidjwoij", "lkdjawlkda", "lkjdawlkdjawlkdj", "jdowaiajowjd"]
        rv = c.post('/movies', json={
            'movieGenres': genres
        })
        answer = movies()
        assert "keinen Film gefunden" in answer


def test_horror_scifi_series():
    with flask_app.test_client() as c:
        genres = ["horror", "sci-fi"]
        rv = c.post('/series', json={
            'movieGenres': genres
        })
        answer = series()
        assert "Rating" in answer and "Dauer" in answer


def test_crime_romance_series():
    with flask_app.test_client() as c:
        genres = ["crime", "romance"]
        rv = c.post('/series', json={
            'movieGenres': genres
        })
        answer = series()
        assert "Rating" in answer and "Dauer" in answer


def test_bad_series():
    with flask_app.test_client() as c:
        genres = ["lkjdddwlkjwdajkldwalkawldkwl", "oidjwoij", "lkdjawlkda", "lkjdawlkdjawlkdj", "jdowaiajowjd"]
        rv = c.post('/series', json={
            'movieGenres': genres
        })
        answer = series()
        assert "keine Serie gefunden" in answer


def test_matches():
    with flask_app.test_client() as c:
        footballClub = "FC Bayern München"
        rv = c.post('/football', json={
            'footballClub': footballClub
        })
        answer = matches()
        assert footballClub in answer and "spielt am" in answer and "Uhr" in answer


def test_bad_matches():
    with flask_app.test_client() as c:
        footballClub = "FC Bielefeld"
        rv = c.post('/football', json={
            'footballClub': footballClub
        })
        answer = matches()
        assert footballClub in answer and "keine geplanten Spiele" in answer


def test_races():
    with flask_app.test_client() as c:
        rv = c.post('/formulaOne', json={

        })
        answer = races()
        assert "Als nächstes" in answer and ":" in answer