from models.test_group import TestGroup
from core.application_data import ApplicationData
import unittest
from unittest.mock import Mock
from models.test_group import TestGroup


class AppData_Should(unittest.TestCase):
    def test_init(self):
        appdata = ApplicationData()

        self.assertIsInstance(appdata._test_groups, list)
        self.assertEqual(0, len(appdata._test_groups))

    def test_groups_access_is_safe_tuple(self):
        appdata = ApplicationData()

        self.assertIsInstance(appdata.groups, tuple)

    def test_addGroup_adds(self):
        appdata = ApplicationData()
        appdata.add_group(Mock(id=1))
        self.assertEqual(1, len(appdata.groups))

    def test_addGroup_returnsFalse_when_tryAdding_same_group(self):
        appdata = ApplicationData()
        group = Mock(id=1)
        appdata.add_group(group)

        self.assertFalse(appdata.add_group(group))

    def test_find_group_returns_correct_groupObject(self):
        appdata = ApplicationData()
        appdata.add_group(Mock(id=1))
        expected = Mock(id=2)
        appdata.add_group(expected)

        actual = appdata.find_group(2)

        self.assertEqual(expected, actual)

    def test_find_group_returns_None_when_absent_id_given(self):
        appdata = ApplicationData()
        appdata.add_group(Mock(id=1))

        self.assertIsNone(appdata.find_group(2))

    def test_remove_group(self):
        appdata = ApplicationData()
        appdata.add_group(Mock(id=1))

        appdata.remove_group(1)

        self.assertEqual(0, len(appdata.groups))

    def test_remove_group_gives_false_when_didnt_find(self):
        appdata = ApplicationData()
        appdata.add_group(Mock(id=1))

        self.assertFalse(appdata.remove_group(2))

    def test_find_test(self):
        appdata = ApplicationData()
        test2 = Mock(id=2)
        appdata.add_group(Mock(id=1, tests=[Mock(id=1), test2]))

        actual = appdata.find_test(2)

        self.assertEqual(test2, actual)

    def test_find_test_returns_None_whne_didntFind(self):
        appdata = ApplicationData()
        appdata.add_group(Mock(id=1, tests=[Mock(id=1), Mock(id=2)]))

        self.assertIsNone(appdata.find_test(3))
