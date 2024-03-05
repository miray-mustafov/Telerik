import unittest

from src.tasks import merge_sorted_lists
from tests.common.list_utils import compare_lists, create_linked_list

class MergeSortedLists_Tests(unittest.TestCase):
    def test_one(self):
        # Arrange
        h1 = create_linked_list(1, 2, 3)
        h2 = create_linked_list(1, 2, 3)
        expected = create_linked_list(1, 1, 2, 2, 3, 3)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))

    def test_two(self):
        # Arrange
        h1 = create_linked_list(1, 2, 3)
        h2 = create_linked_list(1, 2, 3, 4, 5)
        expected = create_linked_list(1, 1, 2, 2, 3, 3, 4, 5)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))

    def test_three(self):
        # Arrange
        h1 = create_linked_list(1, 2, 3)
        h2 = create_linked_list(4, 5, 6)
        expected = create_linked_list(1, 2, 3, 4, 5, 6)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))

    def test_four(self):
        # Arrange
        h1 = create_linked_list(1, 3, 5)
        h2 = create_linked_list(2, 4, 6)
        expected = create_linked_list(1, 2, 3, 4, 5, 6)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))

    def test_five(self):
        # Arrange
        h1 = create_linked_list()
        h2 = create_linked_list(1, 2, 3)
        expected = create_linked_list(1, 2, 3)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))

    def test_six(self):
        # Arrange
        h1 = create_linked_list(1, 2, 3)
        h2 = create_linked_list()
        expected = create_linked_list(1, 2, 3)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))

    def test_seven(self):
        # Arrange
        h1 = create_linked_list(3, 6)
        h2 = create_linked_list(1, 4)
        expected = create_linked_list(1, 3, 4, 6)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))

    def test_eight(self):
        # Arrange
        h1 = create_linked_list(1, 2, 4, 5)
        h2 = create_linked_list(3)
        expected = create_linked_list(1, 2, 3, 4, 5)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))

    def test_nine(self):
        # Arrange
        h1 = create_linked_list(1, 5)
        h2 = create_linked_list(2, 3, 4)
        expected = create_linked_list(1, 2, 3, 4, 5)

        # Act
        merged = merge_sorted_lists(h1, h2)

        # Assert
        self.assertTrue(compare_lists(expected, merged))