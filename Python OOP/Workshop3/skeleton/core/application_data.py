
from models.test_group import TestGroup


class ApplicationData:
    def __init__(self):
        self._test_groups: list[TestGroup] = []

    @property
    def groups(self):
        return tuple(self._test_groups)
