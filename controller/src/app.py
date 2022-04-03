import random

import requests
from flask import Flask, request, jsonify
from SpeechParser import SpeechParser
import config

app = Flask(__name__)


def post_request(usecase_name, route, json_data):
    port = usecase2port[usecase_name]
    url = "http://127.0.0.1:" + str(port) + route
    return requests.post(url, json=json_data)


usecase2port = {
    "controller": 8000,
    "welcome": 8001,
    "entertainment": 8002,
    "finances": 8003,
    "journey": 8004
}


@app.route('/input', methods=['POST'])
def process_text():
    data = request.get_json()
    speech_text = data["speech"]
    # preferences = data["preferences"]

    question = SpeechParser.speech2route(speech_text)
    # if question:
    # Call the matched usecase, and pass the preferences along
    # usecase_response = post_request(question.get_usecase_name(),
    #                               question.get_route(),
    #                               preferences)
    # todo: Error handling
    # tts = usecase_response.text
    # further_questions = question.get_further_questions(4)
    # else:
    #    tts = random.choice(config.no_answer)
    #     further_questions = []

    # response = {
    #    "usecase": question.get_usecase_name(),
    #    "tts": tts,
    #    "further_questions": further_questions
    # }

    if question:
        return jsonify({"route": question.get_route()}), 200
    else:
        return jsonify({"route": "none"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
