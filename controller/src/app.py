import json
import random

import requests
from flask import Flask, request, jsonify
from SpeechParser import SpeechParser
# from ...config import usecase2port, is_production
import config

app = Flask(__name__)

usecase2port = {
    "controller": 8000,
    "welcome": 8001,
    "entertainment": 8002,
    "finances": 8003,
    "journey": 8004
}


def post_request(usecase_name, route, json_data):
    port = usecase2port[usecase_name]
    url = "http://" + usecase_name + ":" + str(port) + route
    # url = "http://localhost:" + str(port) + route
    return requests.post(url, json=json_data)


@app.route('/input', methods=['POST'])
def process_text():
    data = request.get_json()
    speech_text = data["speech"]
    preferences = data["preferences"]

    question = SpeechParser.speech2route(speech_text)
    if question:
        # Call the matched usecase, and pass the preferences along
        usecase_response = post_request(question.get_usecase_name(),
                                        question.get_route(),
                                        preferences)
        # todo: Error handling
        tts = usecase_response.text
        further_questions = question.get_further_questions(4)
        usecase = question.get_usecase_name(),
    else:
        tts = random.choice(config.no_answer)
        further_questions = []
        usecase = "None"

    response = {
        "use_case": usecase,
        "tts": tts,
        "further_questions": further_questions
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
