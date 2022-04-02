from __future__ import annotations

import random
from typing import List


class Question:
    def __init__(self, route: str, keywords: List[str], example_questions: List[str]):
        self._route = route
        self._keywords = keywords
        self._example_questions = example_questions
        self._usecase: Usecase | None = None

    def match_keywords(self, string):
        for keyword in self._keywords:
            if keyword in string:
                return True
        return False

    def get_further_questions(self, n):
        if self._usecase:
            questions = self._usecase.get_questions()
            # select a random question from each question object in the parent usecase, that is not myself
            further_questions = [random.choice(question.get_example_questions())
                                 for question in questions if question != self]
            if len(further_questions) < n:
                return random.choices(further_questions, k=n)
            else:
                return further_questions
        else:
            return []

    def get_route(self):
        return self._route

    def get_example_questions(self):
        return self._example_questions

    def get_keywords(self):
        return self._keywords

    def set_usecase(self, usecase):
        self._usecase = usecase

    def get_usecase_name(self):
        if self._usecase:
            return self._usecase.get_name()
        else:
            return ""


class Usecase:
    def __init__(self, name: str, questions: List[Question]):
        self._name = name
        self._questions = []
        for questions in questions:
            self.add_question(questions)

    def add_question(self, question: Question):
        question.set_usecase(self)
        self._questions.append(question)

    def remove_question(self, index) -> Question:
        return self._questions.pop(index)

    def get_name(self):
        return self._name

    def get_questions(self) -> List[Question]:
        return self._questions
