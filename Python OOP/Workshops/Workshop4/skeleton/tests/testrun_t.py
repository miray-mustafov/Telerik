import unittest
from models.test_run import TestRun
from models.constants.test_result import TestResult

VALID_RUNTIME = 9
VALID_TESTRESULT = TestResult.PASS


class TestRun_Should(unittest.TestCase):
    def test_init_set_props(self):
        trun = TestRun(VALID_TESTRESULT, VALID_RUNTIME)

        self.assertEqual(VALID_TESTRESULT, trun.test_result)
        self.assertEqual(VALID_RUNTIME, trun.runtime_ms)
