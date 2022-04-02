import random

from config import usecases, no_answer


class SpeechParser:
    usecases = usecases

    @staticmethod
    def speech2route(speech_text):
        # return the first match of keywords
        speech_text = speech_text.lower()

        for usecase in usecases:
            for question in usecase.get_questions():
                if question.match_keywords(speech_text):
                    return question
        else:
            return None

    @staticmethod
    def has_overlapping_keywords():
        keywords = []
        # check if there are overlapping keywords
        for usecase in usecases:
            for question in usecase.get_questions():
                for keyword in question.get_keywords():
                    if keyword in keywords:
                        return True
                    else:
                        keywords.append(keyword)
        return False


if __name__ == "__main__":
    speech = "Gib mir ein briefing"
    route = SpeechParser.speech2route(speech)
    if route:
        # Call further routes
        print(route)
    else:
        answer = random.choice(no_answer)
        print(answer)
