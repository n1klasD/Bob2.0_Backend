import pytest
import requests

from ..src.app import post_request, app as flask_app, process_logic
from mock import patch


# pragma: no cover
def test_post_request():
    # create a mock object to test sending requests
    with patch("requests.post") as patched_post:
        json_data = {"p1": 1}
        post_request("welcome", "/briefing", json_data)
        patched_post.assert_called_once_with("http://welcome:8001/briefing", json=json_data)


# ------ test flask app ------ #

# pragma: no cover
@pytest.fixture()
def app():
    yield flask_app


# pragma: no cover
@pytest.fixture()
def client(app):
    return app.test_client()


# pragma: no cover
def test_input_request(client):
    # mock the request to the welcome usecase and change the response
    with patch("requests.post") as patched_post:
        response = requests.Response()
        response._content = "Mock tts".encode("utf-8")
        patched_post.return_value = response

        # send request to test client
        response = client.post("/input", json=
        {
            "speech": "Was ist mein briefing?",
            "preferences": {
                "p1": 0,
                "p2": 1
            }
        })

        assert response.json["tts"] == "Mock tts" and response.status_code == 200


# Test the processing logic
# pragma: no cover
def test_process_logic():
    with patch("requests.post") as patched_post:
        response = requests.Response()
        response._content = "Mock tts".encode("utf-8")
        patched_post.return_value = response

        json_response = process_logic("Briefing", {"p1": 0})
        assert json_response["tts"] == "Mock tts"
