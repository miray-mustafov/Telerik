import unittest

from src.tasks import find_middle_of_list
from tests.common.list_utils import create_linked_list


class FindMiddleOfList_Tests(unittest.TestCase):
    def test_one(self):
        # Arrange
        test = create_linked_list(1, 2, 3)
        expected_middle = test.next

        # Act
        middle_node = find_middle_of_list(test)

        # Assert
        self.assertEqual(expected_middle, middle_node)

    def test_two(self):
        # Arrange
        test = create_linked_list(1, 2, 3, 4)
        expected_middle = test.next.next

        # Act
        middle_node = find_middle_of_list(test)

        # Assert
        self.assertEqual(expected_middle, middle_node)

    def test_three(self):
        # Arrange
        test = create_linked_list(1)
        expected_middle = test

        # Act
        middle_node = find_middle_of_list(test)

        # Assert
        self.assertEqual(expected_middle, middle_node)

    def test_four(self):
        # Arrange
        test = create_linked_list(5, 5, 5, 5, 5)
        expected_middle = test.next.next

        # Act
        middle_node = find_middle_of_list(test)

        # Assert
        self.assertEqual(expected_middle, middle_node)
