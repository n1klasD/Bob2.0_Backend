
from typing import List


from controller.src.ControllerDefinitions import Usecase


class SpeechParser:
    def __init__(self, usecase: List[Usecase]):
        self._usecases = usecase

    def speech2route(self, speech_text):
        """
        Assign a route based on keywords in speech_text

        :param speech_text:
        :return: Question | None
        """

        # return the first match of keywords
        speech_text = speech_text.lower()

        for usecase in self._usecases:
            for question in usecase.get_questions():
                if question.match_keywords(speech_text):
                    return question
        else:
            return None

    def has_overlapping_keywords(self):
        """
        Check, if the usecases have overlapping keywords

        :return: bool
        """

        keywords = []
        # check if there are overlapping keywords
        for usecase in self._usecases:
            for question in usecase.get_questions():
                for keyword in question.get_keywords():
                    if keyword in keywords:
                        return True
                    else:
                        keywords.append(keyword)
        return False
