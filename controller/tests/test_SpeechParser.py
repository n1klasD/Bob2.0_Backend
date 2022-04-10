import pytest

from ..src.ControllerDefinitions import Usecase, Question
from ..src.SpeechParser import SpeechParser


@pytest.fixture
def example_usecase():
    usecases = [
        Usecase(
            name="welcome",
            questions=[
                Question(
                    route="/welcome",
                    keywords=["willkommen", "guten morgen", "briefing", "briefing"],
                    example_questions=["Gib mir ein Briefing für den Tag", "Zeig mir den guten Morgen Dialog"]
                )
            ]
        )
    ]
    return usecases


def test_speech2route(example_usecase):
    parser = SpeechParser(example_usecase)
    speech = "Guten Morgen!"
    question = parser.speech2route(speech)
    assert question.get_route() == "/welcome"


def test_has_overlapping_keywords(example_usecase):
    parser = SpeechParser(example_usecase)
    assert parser.has_overlapping_keywords() == True
