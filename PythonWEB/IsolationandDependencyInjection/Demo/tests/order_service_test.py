import unittest
from unittest.mock import Mock, create_autospec, patch
from data.models import Order
from services import order_service

mock_db = Mock()
order_service.database = mock_db
FAKE_ORDERS = [
    (1, '2021-01-01', 'Svishtov', 2, 1),
    (1, '2021-01-01', 'Svishtov', 2, 2),
    (3, '2021-01-02', 'Pleven', 3, 3),
]


class OrderService_Should(unittest.TestCase):

    def test_all_createsListOfOrders_when_dataIsPresent(self):
        get_data_func = lambda q: FAKE_ORDERS
        result = list(order_service.all(get_data_func))
        self.assertEqual(2, len(result))

    def test_all_createsListOfOrders_when_dataIsPresent_withMock(self):
        mock_db.read_query.return_value = FAKE_ORDERS
        result = list(order_service.all())

        self.assertEqual(2, len(result))

    # def test_all_createsListOfCategories_when_dataIsPresent_withPatch(self):
    #     with patch('services.category_service.database') as mock_db:
    #         mock_db.read_query.return_value = [(1, 'TV'), (2, 'Computers')]
    #         result = list(category_service.all())
    #
    #     self.assertEqual(2, len(result))
