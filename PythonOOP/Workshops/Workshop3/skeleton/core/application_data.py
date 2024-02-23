from typing import List
from models.constants.test_result import TestResult
from models.test_group import TestGroup
from models.test import Test
from models.test_run import TestRun


class ApplicationData:
    def __init__(self):
        self._test_groups: List[TestGroup] = []
        self._tests: List[Test] = []
        self._test_runs: List[TestRun] = []  # !

    @property
    def test_groups(self):
        return tuple(self._test_groups)

    @property
    def tests(self):
        return tuple(self._tests)

    @property
    def test_runs(self):
        return tuple(self._test_runs)

    def find_testgroup_by_id(self, tgroup_id):
        for tgroup in self._test_groups:
            if tgroup.id == tgroup_id:
                return tgroup
        raise ValueError(f"Testgroup id:{tgroup_id} not found!")

    def find_test_by_id(self, test_id):
        for tst in self._tests:
            if tst.id == test_id:
                return tst
        raise ValueError(f"Test id:{test_id} not found!")

    def create_and_add_trun_to_test(self, test_id, test_result, runtime_ms):  # !
        tst = self.find_test_by_id(test_id)
        trun = TestRun(test_id, test_result, runtime_ms)
        tst.add_test_run(trun)
        self._test_runs.append(trun)
        return

    def create_and_add_test_to_tgroup(self, tgroup_id, descrp):  # !
        tgroup = self.find_testgroup_by_id(tgroup_id)
        tst = Test(tgroup_id, descrp)
        tgroup.add_test(tst)
        self._tests.append(tst)
        return tst

    def add_testgroup(self, name):
        tgroup: TestGroup = TestGroup(name)
        self._test_groups.append(tgroup)
        return tgroup

    def remove_group_by_id(self, tgroup_id):
        tgroup_to_remove = self.find_testgroup_by_id(tgroup_id)
        tests_to_remove = tgroup_to_remove._tests

        for tst in tests_to_remove:  # accessing all truns
            for trun in tst._test_runs:
                self._test_runs.remove(trun)  # clean references to the specified truns from appdata
        for tst in tests_to_remove:  # access all tests
            self._tests.remove(tst)  # clean them one by one from app data
        self._test_groups.remove(tgroup_to_remove)  # removing the group from appdata

        del tests_to_remove
        del tgroup_to_remove

    def report_test(self, test_id):
        tst: Test = self.find_test_by_id(test_id)
        runs_count, passing, failing, total_runtime = len(tst.test_runs), 0, 0, 0
        res = f'#{tst.id}. [{tst.description}]: {runs_count} runs'
        for trun in tst.test_runs:
            if trun.test_result == TestResult.PASS:
                passing += 1
            elif trun.test_result == TestResult.FAIL:
                failing += 1
            total_runtime += trun.runtime_ms
        res += f'\n- Passing: {passing}'
        res += f'\n- Failing: {failing}'
        res += f'\n- Total runtime: {total_runtime}ms'
        if not runs_count:
            avg = 0
        else:
            avg = total_runtime / runs_count
        res += f'\n- Average runtime: {avg:.1f}ms'
        return res

    def view_group(self, tgroup_id):
        tgroup = self.find_testgroup_by_id(tgroup_id)
        res = f'#{tgroup.id}. {tgroup.name} ({len(tgroup.tests)} tests)'
        for tst in tgroup.tests:
            res += f"\n  #{tst.id}. [{tst.description}]: {len(tst.test_runs)} runs"

        return res

    def view_system(self):
        res = f'Test Reporter System ({len(self._test_groups)} test groups)'
        for tgroup in self.test_groups:
            res += f"\n  #{tgroup.id}. {tgroup.name} ({len(tgroup.tests)} tests)"

        return res
