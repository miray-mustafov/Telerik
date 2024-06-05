import unittest
from unittest.mock import Mock, patch
from common.responses import Unauthorized
from data.models import User
from routers import orders as orders_router


mock_product_service = Mock(spec='services.product_service')
mock_order_service = Mock(spec='services.order_service')
mock_users_service = Mock(spec='services.users_service')

orders_router.product_service = mock_product_service
orders_router.order_service = mock_order_service
orders_router.users_service = mock_users_service


def fake_order():
    order = Mock()

    return order


def fake_admin():
    admin = Mock()
    admin.is_admin = lambda: True

    return admin


def fake_user():
    admin = Mock()
    admin.is_admin = lambda: False

    return admin


class OrdersRouter_Should(unittest.TestCase):

    def setUp(self) -> None:
        mock_order_service.reset_mock()
        mock_product_service.reset_mock()
        mock_users_service.reset_mock()

    def test_getOrders_returnsAllOrders_whenUserIsAdmin(self):
        with patch('routers.orders.get_user_or_raise_401') as get_user_func:
            # Arrange
            test_orders = [fake_order(), fake_order()]
            get_user_func.return_value = fake_admin()
            mock_order_service.all = lambda: test_orders

            # Act
            result = orders_router.get_orders()

            # Assert
            self.assertEqual(test_orders, result)

    def test_getOrders_returnsUnauthorized_whenUserIsNotAdmin(self):
        with patch('routers.orders.get_user_or_raise_401') as get_user_func:
            # Arrange
            get_user_func.return_value = fake_user()

            # Act
            result = orders_router.get_orders()

            # Assert
            self.assertIsInstance(result, Unauthorized)

    def test_getOrders_returnsSortedOrders_whenOptionalParamsAreCorrect(self):
        with patch('routers.orders.get_user_or_raise_401') as get_user_func:
            # Arrange
            test_orders = [fake_order(), fake_order()]
            sorted_orders = [fake_order(), fake_order()]
            get_user_func.return_value = fake_admin()
            mock_order_service.all = lambda: test_orders
            mock_order_service.sort = lambda orders, reverse: sorted_orders

            # Act
            resultAsc = orders_router.get_orders('asc')
            resultDesc = orders_router.get_orders('desc')

            # Assert
            self.assertEqual(sorted_orders, resultAsc)
            self.assertEqual(sorted_orders, resultDesc)

    def test_getOrders_returnsUnsortedOrders_whenOptionalParamIsNotCorrect(self):
        with patch('routers.orders.get_user_or_raise_401') as get_user_func:
            # Arrange
            test_orders = [fake_order(), fake_order()]
            get_user_func.return_value = fake_admin()
            mock_order_service.all = lambda: test_orders

            # Act
            result = orders_router.get_orders('not asc or desc')

            # Assert
            self.assertEqual(test_orders, result)
