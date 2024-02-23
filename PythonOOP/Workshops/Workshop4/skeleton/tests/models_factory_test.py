import unittest
from core.models_factory import ModelsFactory
from models.test_group import TestGroup
from models.test import Test
from models.test_run import TestRun
from models.constants.test_result import TestResult
from errors.application_error import ApplicationError


class ModelsFactory_Should(unittest.TestCase):
    def test_init_sets(self):
        mf = ModelsFactory()
        self.assertEqual(1, mf._test_group_id)
        self.assertEqual(1, mf._test_id)

    def test_create_group(self):
        mf = ModelsFactory()
        group = mf.create_group('name')

        self.assertEqual(2, mf._test_group_id)
        self.assertIsInstance(group, TestGroup)

    def test_create_test(self):
        mf = ModelsFactory()
        test = mf.create_test('description')

        self.assertEqual(2, mf._test_id)
        self.assertIsInstance(test, Test)

    def test_create_test_run(self):
        mf = ModelsFactory()
        trun = mf.create_test_run('pass', '25')

        self.assertIsInstance(trun, TestRun)

    def test_create_test_run_raiseError_when_wrong_tresult_given(self):
        mf = ModelsFactory()
        with self.assertRaises(ApplicationError):
            mf.create_test_run('passss', '25')

    def test_create_test_run_raiseError_when_wrong_runtimems_given(self):
        mf = ModelsFactory()
        with self.assertRaises(ApplicationError):
            mf.create_test_run('pass', '25.OA')