from typing import List, TYPE_CHECKING
from models.constants.test_result import TestResult
from models.test_run import TestRun

if TYPE_CHECKING:
    pass


class Test:
    ID = 1

    def __init__(self, group_id, description: str):
        self._description = description
        self._test_runs: List[TestRun] = []
        self._test_group_id = group_id  # !
        self._id = Test.ID
        Test.ID += 1

    @property
    def id(self):
        return self._id

    @property
    def test_group_id(self):
        return self._test_group_id

    @property
    def description(self):
        return self._description

    @property
    def test_runs(self):
        return tuple(self._test_runs)

    def add_test_run(self, test_run: TestRun):
        self._test_runs.append(test_run)

    def __repr__(self):
        return f"T{self.id} {self.description[:5]}..."
