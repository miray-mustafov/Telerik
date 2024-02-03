import unittest
from models.test_group import TestGroup
from models.constants.test_result import TestResult
from errors.application_error import ApplicationError
from unittest.mock import Mock
from models.test import Test

ID = 1
VALID_NAME = 'NAME'


class TestRun_Should(unittest.TestCase):
    def test_init_set_props(self):
        tgroup = TestGroup(ID, VALID_NAME)

        self.assertEqual(ID, tgroup.id)
        self.assertEqual(VALID_NAME, tgroup.name)

    def test_init_raise_error_invalid_name(self):
        with self.assertRaises(ApplicationError):
            TestGroup(ID, '')

    def test_instanceTests_return_tuple(self):
        tgroup = TestGroup(ID, VALID_NAME)
        self.assertIsInstance(tgroup.tests, tuple, 'test msg')

    def test_addTest_adds_when_unique_test_given(self):
        tgroup = TestGroup(ID, VALID_NAME)
        test = Mock(id=2)

        tgroup.add_test(test)

        self.assertEqual(1, len(tgroup.tests))

    def test_addTest_doesNothing_when_similar_test_given(self):
        tgroup = TestGroup(ID, VALID_NAME)
        test = Mock(id=1)
        tgroup.add_test(test)
        tgroup.add_test(test)

        self.assertEqual(1, len(tgroup.tests))

    def test_view_returns_correct_output_with_some_tests(self):
        tgroup = TestGroup(ID, VALID_NAME)
        tgroup.add_test(Test(2, 'desc'))

        expected = '#1. NAME (1 tests)\n  #2. [desc]: 0 runs'
        actual = tgroup.view()

        self.assertEqual(expected, actual)

    def test_view_returns_correct_output_with_zero_tests(self):
        tgroup = TestGroup(ID, VALID_NAME)

        expected = '#1. NAME (0 tests)'
        actual = tgroup.view()

        self.assertEqual(expected, actual)

    def test_str_returns_correctly(self):
        tgroup = TestGroup(ID, VALID_NAME)
        expected = f'#{ID}. {VALID_NAME} (0 tests)'
        self.assertEqual(expected, str(tgroup))
