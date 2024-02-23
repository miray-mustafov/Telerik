import unittest
from models.test import Test
from models.test_run import TestRun
from models.constants.test_result import TestResult
from errors.application_error import ApplicationError
from unittest.mock import Mock

ID = 1
VALID_DESC = 'Description'


class Test_Should(unittest.TestCase):
    def test_init_set_props(self):
        test = Test(ID, VALID_DESC)

        self.assertEqual(ID, test.id)
        self.assertEqual(VALID_DESC, test.description)

    def test_init_raiseError_when_invalid_description(self):
        with self.assertRaises(ApplicationError):
            Test(ID, '')

    def test_testruns_return_tuple(self):
        test = Test(ID, VALID_DESC)
        self.assertIsInstance(test.test_runs, tuple)

    def test_addTestRun_adds(self):
        trun = Mock()
        test = Test(ID, VALID_DESC)
        test.add_test_run(trun)

        self.assertEqual((trun,), test.test_runs)

    def test_addTestRun_adds_two_similar(self):
        trun = Mock()
        test = Test(ID, VALID_DESC)
        test.add_test_run(trun)
        test.add_test_run(trun)

        self.assertEqual(2, len(test.test_runs))

    def test_passingTestRuns_returns_tuple(self):
        test = Test(ID, VALID_DESC)
        self.assertIsInstance(test.passing_test_runs, tuple)

    def test_passingTestRuns_returns_only_passing(self):
        test = Test(ID, VALID_DESC)
        trun_failed = Mock(test_result=TestResult.FAIL)
        trun_passed = Mock(test_result=TestResult.PASS)

        test.add_test_run(trun_failed)
        test.add_test_run(trun_passed)

        self.assertEqual(1, len(test.passing_test_runs))
        self.assertEqual(trun_passed, test.passing_test_runs[0])

    def test_failingTestRuns_returns_tuple(self):
        test = Test(ID, VALID_DESC)
        self.assertIsInstance(test.failed_test_runs, tuple)

    def test_failingTestRuns_returns_only_passing(self):
        test = Test(ID, VALID_DESC)
        trun_failed = Mock(test_result=TestResult.FAIL)
        trun_passed = Mock(test_result=TestResult.PASS)

        test.add_test_run(trun_failed)
        test.add_test_run(trun_passed)

        self.assertEqual(1, len(test.failed_test_runs))
        self.assertEqual(trun_failed, test.failed_test_runs[0])

    def test_total_runtime_works(self):
        test = Test(ID, VALID_DESC)
        test.add_test_run(Mock(runtime_ms=20))
        test.add_test_run(Mock(runtime_ms=40))

        self.assertEqual(60, test.total_runtime)

    def test_avg_runtime_handles_zeroDivision(self):
        test = Test(ID, VALID_DESC)

        self.assertEqual(0.0, test.avg_runtime)

    def test_avg_runtime_returns_correctly(self):
        test = Test(ID, VALID_DESC)
        test.add_test_run(Mock(runtime_ms=6))
        test.add_test_run(Mock(runtime_ms=5))

        self.assertEqual(5.5, test.avg_runtime)

    def test_str_works(self):
        test = Test(ID, VALID_DESC)
        test.add_test_run(Mock())
        expected = f'#{ID}. [{VALID_DESC}]: {1} runs'
        self.assertEqual(expected, str(test))

    def test_generate_report_with_zero_truns(self):
        test = Test(ID, VALID_DESC)
        expected = f'#{ID}. [{VALID_DESC}]: {0} runs'
        self.assertEqual(expected, test.generate_report())

    def test_generate_report_with_2_truns(self):
        test = Test(ID, VALID_DESC)
        test.add_test_run(TestRun(TestResult.PASS, 5))
        test.add_test_run(TestRun(TestResult.FAIL, 5))
        expected = '\n'.join([
            f'{str(test)}',
            f'- Passing: {len(test.passing_test_runs)}',
            f'- Failing: {len(test.failed_test_runs)}',
            f'- Total runtime: {test.total_runtime}ms',
            f'- Average runtime: {test.avg_runtime:.1f}ms'
        ])
        self.assertEqual(expected, test.generate_report())

    def test_generate_report_with_correctly_formatted_avg(self):
        test = Test(ID, VALID_DESC)
        test.add_test_run(TestRun(TestResult.PASS, 5.5))
        test.add_test_run(TestRun(TestResult.FAIL, 5))
        expected = '\n'.join([
            f'{str(test)}',
            f'- Passing: {len(test.passing_test_runs)}',
            f'- Failing: {len(test.failed_test_runs)}',
            f'- Total runtime: {test.total_runtime}ms',
            f'- Average runtime: {test.avg_runtime:.1f}ms'
        ])
        self.assertEqual(expected, test.generate_report())
