import unittest

from src.tasks import backspace_char


class BackspaceChar_Test(unittest.TestCase):
    def test_one(self):
        # Arrange
        test = 'abc#d'
        expected = 'abd'

        # Act
        actual = backspace_char(test)

        # Assert
        self.assertEqual(expected, actual)

    def test_two(self):
        # Arrange
        test = 'abcd##e##'
        expected = 'a'

        # Act
        actual = backspace_char(test)

        # Assert
        self.assertEqual(expected, actual)

    def test_three(self):
        # Arrange
        test = 'abc####de'
        expected = 'de'

        # Act
        actual = backspace_char(test)

        # Assert
        self.assertEqual(expected, actual)

    def test_four(self):
        # Arrange
        test = 'teler#ric#k'
        expected = 'telerik'

        # Act
        actual = backspace_char(test)

        # Assert
        self.assertEqual(expected, actual)

    def test_five(self):
        # Arrange
        test = 'jav##ava###script#####'
        expected = 'js'

        # Act
        actual = backspace_char(test)

        # Assert
        self.assertEqual(expected, actual)
