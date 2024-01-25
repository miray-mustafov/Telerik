from typing import List, TYPE_CHECKING

from models.test import Test


class TestGroup:
    ID = 1

    def __init__(self, name: str):
        self._name = name
        self._tests: List[Test] = []
        self._id = TestGroup.ID
        TestGroup.ID += 1

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def tests(self):
        return tuple(self._tests)

    def add_test(self, test: Test):
        self._tests.append(test)

    def __repr__(self):
        return f"TG{self.id} {self.name}"
