import pytest

from ..src import Usecase, Question


# ----------------------- [Question] ---------------------- #

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
                ),
                Question(
                    route="/stundenplan",
                    keywords=["stundenplan", "rapla", "vorlesungen", "vorlesung"],
                    example_questions=["Wann habe ich heute Vorlesung?", "Was steht im Stundenplan?"]
                )
            ]
        )
    ]
    return usecases


@pytest.fixture()
def question():
    question = Question(
        keywords=["test1", "test2"],
        example_questions=["q1"],
        route="/test"
    )
    return question


# tests if keyword match is detected in string
def test_match_keywords_positive(question):
    assert question.match_keywords("hello test1") == True


# test if correct number of example questions is returned, when n is bigger than the number of available ones
def test_get_further_questions_bigger_than_available(example_usecase):
    question1 = example_usecase[0].get_questions()[0]
    further_questions = question1.get_further_questions(3)
    assert len(further_questions) == 1


# test if correct number of example questions is returned, when n is 0
def test_get_further_questions_n_0(example_usecase):
    question1 = example_usecase[0].get_questions()[0]
    further_questions = question1.get_further_questions(0)
    assert len(further_questions) == 0


def test_get_example_questions(question):
    assert question.get_example_questions() == ["q1"]


def test_get_route(question):
    assert question.get_route() == "/test"


@pytest.fixture()
def dummy_usecase():
    return Usecase(name="", questions=[])


def test_set_usecase(question):
    question.set_usecase(dummy_usecase)
    assert question._usecase == dummy_usecase


# ----------------------- [Usecase] ------------------------ #

def test_add_question(dummy_usecase, question):
    dummy_usecase.add_question(question)
    new_question = dummy_usecase.get_questions()[0]

    assert new_question == question and question._usecase == dummy_usecase


def test_get_name(dummy_usecase):
    assert dummy_usecase.get_name() == ""


def test_remove_question(dummy_usecase, question):
    dummy_usecase.add_question(question)
    dummy_usecase.remove_question(0)
    assert len(dummy_usecase.get_questions()) == 0
