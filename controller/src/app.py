import random

import requests
from flask import Flask, request, jsonify
from controller.src.SpeechParser import SpeechParser
import config as config

app = Flask(__name__)


def post_request(usecase_name, route, json_data):
    """
    This methods posts a request to http://usecase_name:usecase_port/route.
    This is used for the controller to communicate with other containers.

    :param usecase_name: the usecase name
    :param route: The route of the service
    :param json_data: The data to be send
    :return: request.Response
    """

    usecase2port = {
        "controller": 8000,
        "welcome": 8001,
        "entertainment": 8002,
        "finances": 8003,
        "journey": 8004
    }

    port = usecase2port[usecase_name]
    url = "http://" + usecase_name + ":" + str(port) + route
    # url = "http://localhost:" + str(port) + route
    return requests.post(url, json=json_data)


def process_logic(speech_text, preferences):
    # create a speech parser with the usecase definition from config
    speech_parser = SpeechParser(usecase=config.usecases)

    # select a route that corresponds to the keywords
    question = speech_parser.speech2route(speech_text)
    if question:
        # Call the matched usecase, and pass the preferences along
        usecase_response = post_request(question.get_usecase_name(),
                                        question.get_route(),
                                        preferences)
        tts = usecase_response.text
        further_questions = question.get_further_questions(4)
        usecase = question.get_usecase_name(),
    else:
        # select a random answer string
        tts = random.choice(config.no_answer)
        further_questions = []
        usecase = "None"

    # craft the response object
    response = {
        "use_case": usecase,
        "tts": tts,
        "further_questions": further_questions
    }
    return response


@app.route('/input', methods=['POST'])
def process_text():
    """
        Route that serves the /input directive
    """

    data = request.get_json()
    speech_text = data["speech"]
    preferences = data["preferences"]

    response = process_logic(speech_text, preferences)

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
