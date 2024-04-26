import unittest
from unittest.mock import Mock, create_autospec, patch
from data.models import Category
from services import category_service

# mock_db = Mock()
# category_service.database = mock_db


class CategoryService_Should(unittest.TestCase):

    def test_all_createsListOfCategories_when_dataIsPresent(self):
        get_data_func = lambda q: [(1, 'TV'), (2, 'Computers')]
        result = list(category_service.all(get_data_func))
        self.assertEqual(2, len(result))

    # def test_all_createsListOfCategories_when_dataIsPresent_withMock(self):
    #     mock_db.read_query.return_value = [(1, 'TV'), (2, 'Computers')]
    #     result = list(category_service.all())

    #     self.assertEqual(2, len(result))

    def test_all_createsListOfCategories_when_dataIsPresent_withPatch(self):
        with patch('services.category_service.database') as mock_db:
            mock_db.read_query.return_value = [(1, 'TV'), (2, 'Computers')]
            result = list(category_service.all())

        self.assertEqual(2, len(result))


    @patch('services.category_service.database', autospec=True)
    def test_all_createsListOfCategories_when_dataIsPresent_withPatch_v2(self, mock_db):
        mock_db.read_query.return_value = [(1, 'TV'), (2, 'Computers')]
        result = list(category_service.all())
        self.assertEqual(2, len(result))


    def test_all_createsEmptyList_when_noData(self):
        get_data_func = lambda q: []
        result = list(category_service.all(get_data_func))
        expected = []
        self.assertEqual(expected, result)


    def test_getById_returns_singleCategory_when_dataIsPresent(self):
        get_data_func = lambda q, id: [(1, 'TV')]
        result = category_service.get_by_id(1, get_data_func)
        expected = Category(id=1, name='TV')
        self.assertEqual(expected, result)


    def test_getById_returns_None_when_noData(self):
        get_data_func = lambda q, id: []
        result = category_service.get_by_id(1, get_data_func)
        expected = None
        self.assertEqual(expected, result)

    def test_exists_returns_True_when_dataIsPresent(self):
        get_data_func = lambda q, id: [(1, 'TV')]
        result = category_service.exists(1, get_data_func)
        expected = True
        self.assertEqual(expected, result)

    def test_exists_returns_False_when_noData(self):
        get_data_func = lambda q, id: []
        result = category_service.exists(1, get_data_func)
        expected = False
        self.assertEqual(expected, result)

    def test_create_returns_categoryWithGeneratedId(self):
        generated_id = 2
        insert_data_func = lambda q, cat: generated_id
        result = category_service.create(Category(id=None,name='TV'), insert_data_func)
        expected = Category(id=generated_id, name='TV')
        self.assertEqual(expected, result)  
        