from typing import List

from models.test_group import TestGroup
from models.test import Test
from models.test_run import TestRun


class ApplicationData:
    def __init__(self):
        self._test_groups: List[TestGroup] = []
        self._tests: List[Test] = []
        self._test_runs: List[TestRun] = []  # !

    @property
    def groups(self):
        return tuple(self._test_groups)

    def create_and_add_trun_to_test(self, test_id, test_result, runtime_ms):  # !
        for tst in self._tests:
            if tst.id == test_id:
                trun = TestRun(test_id, test_result, runtime_ms)
                tst.add_test_run(trun)
                self._test_runs.append(trun)
                return
        raise ValueError(f'Test with id:{test_id} doesn\'t exist in the application data!')

    def create_and_add_test_to_tgroup(self, tgroup_id, descrp):  # !
        for tgroup in self._test_groups:
            if tgroup.id == tgroup_id:
                tst = Test(tgroup_id, descrp)
                tgroup.add_test(tst)
                self._tests.append(tst)
                return tst
        raise ValueError(f"Test group with id:{tgroup_id} doesn\'t exist in the application data!")

    def add_testgroup(self, name):
        tgroup = TestGroup(name)
        self._test_groups.append(tgroup)
        return tgroup

    def find_testgroup_by_id(self, tgroup_id):
        pass

    def remove_testgroup_by_id(self, tgroup_id):
        pass

    def find_test_by_id(self, test_id):
        pass
