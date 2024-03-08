import unittest

from src.tasks import reverse_list
from tests.common.list_utils import compare_lists, create_linked_list


class ReverseLists_Tests(unittest.TestCase):
    def test_one(self):
        # Arrange
        list = create_linked_list(1, 2, 3)
        expected = create_linked_list(3, 2, 1)

        # Act
        reversed = reverse_list(list)

        # Assert
        self.assertTrue(compare_lists(expected, reversed))

    def test_two(self):
        # Arrange
        list = create_linked_list(1, 2, 3, 4)
        expected = create_linked_list(4, 3, 2, 1)

        # Act
        reversed = reverse_list(list)

        # Assert
        self.assertTrue(compare_lists(expected, reversed))

    def test_three(self):
        # Arrange
        list = create_linked_list(1, 2)
        expected = create_linked_list(2, 1)

        # Act
        reversed = reverse_list(list)

        # Assert
        self.assertTrue(compare_lists(expected, reversed))

    def test_four(self):
        # Arrange
        list = create_linked_list(1)
        expected = create_linked_list(1)

        # Act
        reversed = reverse_list(list)

        # Assert
        self.assertTrue(compare_lists(expected, reversed))

    def test_five_empty_lists(self):
        # Arrange
        list = create_linked_list()
        expected = create_linked_list()

        # Act
        reversed = reverse_list(list)

        # Assert
        self.assertTrue(compare_lists(expected, reversed))
