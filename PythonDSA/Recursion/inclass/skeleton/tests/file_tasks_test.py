import unittest
from os import path
import src.tasks as file_tasks

def get_test_path():
    cwd = path.dirname(__file__)
    return path.join(cwd, 'demo_folder')


class FileTaskTests(unittest.TestCase):
    def test_traverse_directories(self):
        # Arrange
        expected = ['demo_folder', 'nested-1', 'file-1.md', 'file-2.md', 'file-3.md',
                    'nested-1-1', 'example.txt', 'nested-2', 'test-1.csv', 'test-2.txt', 'test-3.md']
        test_file_path = get_test_path()

        # Act
        actual = file_tasks.traverse_directories(test_file_path)

        # Assert
        self.assertEqual(sorted(expected), sorted(actual))

    def test_find_files_ext1(self):
        # Arrange
        expected = ['file-1.md', 'file-2.md', 'file-3.md', 'test-3.md']
        test_file_path = get_test_path()

        # Act
        actual = file_tasks.find_files(test_file_path, 'md')

        # Assert
        self.assertEqual(sorted(expected), sorted(actual))

    def test_find_files_ext2(self):
        # Arrange
        expected = ['example.txt', 'test-2.txt']
        test_file_path = get_test_path()

        # Act
        actual = file_tasks.find_files(test_file_path, 'txt')

        # Assert
        self.assertEqual(sorted(expected), sorted(actual))

    def test_file_exists_returnsTrue_file1(self):
        # Arrange
        test_file_path = get_test_path()

        # Act & Assert
        self.assertTrue(file_tasks.file_exists(test_file_path, 'file-1.md'))

    def test_file_exists_returnsTrue_file2(self):
        # Arrange
        test_file_path = get_test_path()

        # Act & Assert
        self.assertTrue(file_tasks.file_exists(test_file_path, 'example.txt'))

    def test_file_exists_returnsTrue_file3(self):
        # Arrange
        test_file_path = get_test_path()

        # Act & Assert
        self.assertFalse(file_tasks.file_exists(
            test_file_path, 'examplee.txt'))

    def test_directory_stats(self):
        # Arrange
        expected = {'.md': 4, '.txt': 2, '.csv': 1}
        test_file_path = get_test_path()

        # Act
        actual = file_tasks.directory_stats(test_file_path)

        # Assert
        self.assertDictEqual(expected, actual)
