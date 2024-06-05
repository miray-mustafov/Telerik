from datetime import date
import unittest
from unittest.mock import patch
from data.models import Order, OrderResponse, OrderUpdate, Product, User
from services import order_service as service

TEST_DATE = date(1111, 1, 1)
TEST_ADDRESS = 'addr'
TEST_USER_ID = 2


def create_order(order_id, product_ids=[]):
    return Order(
        id=order_id,
        product_ids=product_ids,
        delivery_date=TEST_DATE,
        delivery_address=TEST_ADDRESS,
        user_id=TEST_USER_ID)


class OrdersService_Should(unittest.TestCase):

    def test_getById_returnsCorrectOrder(self):
        with patch('services.order_service.read_query') as get_order_func:
            # Arrange
            test_id = 5
            get_order_func.return_value = [
                (test_id, TEST_DATE, TEST_ADDRESS, TEST_USER_ID)]
            expected = create_order(test_id)

            # Act
            result = service.get_by_id(test_id)

            # Assert
            self.assertEqual(expected, result)

    def test_getById_returnsNone(self):
        with patch('services.order_service.read_query') as get_order_func:
            # Arrange
            get_order_func.return_value = []

            # Act
            result = service.get_by_id(5)

            # Assert
            self.assertIsNone(result)

    def test_all_returnsOrdersWithProducts(self):
        with patch('services.order_service.read_query') as get_order_func:
            # Arrange
            order1_id, order2_id = 10, 20
            product1_id, product2_id, product3_id = 3, 4, 5
            get_order_func.return_value = [
                (order1_id, TEST_DATE, TEST_ADDRESS, TEST_USER_ID, product1_id),
                (order1_id, TEST_DATE, TEST_ADDRESS, TEST_USER_ID, product2_id),
                (order2_id, TEST_DATE, TEST_ADDRESS, TEST_USER_ID, product3_id),
            ]
            expected = [
                create_order(order1_id, [product1_id, product2_id]),
                create_order(order2_id, [product3_id])
            ]

            # Act
            result = service.all()

            # Assert
            self.assertEqual(expected, list(result))

    def test_sort_returnsOrdersByDateAscending(self):
        A = create_order(1)
        A.delivery_date = date(2000, 1, 1)
        B = create_order(2)
        B.delivery_date = date(1000, 1, 1)
        C = create_order(3)
        C.delivery_date = date(3000, 1, 1)

        test = [A, B, C]
        expected = [B, A, C]

        # Act
        result = service.sort(test)

        # Assert
        self.assertEqual(expected, result)

    def test_sort_returnsOrdersByDateDescending(self):
        A = create_order(1)
        A.delivery_date = date(2000, 1, 1)
        B = create_order(2)
        B.delivery_date = date(1000, 1, 1)
        C = create_order(3)
        C.delivery_date = date(3000, 1, 1)

        test = [A, B, C]
        expected = [C, A, B]

        # Act
        result = service.sort(test, reverse=True)

        # Assert
        self.assertEqual(expected, result)

    def test_createResponseObject_returnsCorrectOrderTotal_withoutFee(self):
        # Arrange
        test_order = create_order(1)
        test_customer = User(id=None,username='test', password='test', role='user')
        test_products = [
            Product(id=None, name='n1', description='d1', price=100.0, category_id=1),
            Product(id=None, name='n2', description='d2', price=25.0, category_id=2),
        ]

        expected = OrderResponse(
            id=test_order.id,
            customer=test_customer,
            products=test_products,
            delivery_address=TEST_ADDRESS,
            delivery_date=TEST_DATE,
            order_total=(100.0 + 25.0)
        )

        # Act
        result = service.create_response_object(
            test_customer, test_order, test_products)

        # Assert
        self.assertEqual(expected, result)

    def test_createResponseObject_returnsCorrectOrderTotal_withFee(self):
        # Arrange
        test_order = create_order(1)
        test_customer = User(id=None,username='test', password='test', role='user')
        test_products = [
            Product(id=None, name='n1', description='d1', price=100.0, category_id=1),
            Product(id=None, name='n2', description='d2', price=26.0, category_id=2),
        ]

        expected = OrderResponse(
            id=test_order.id,
            customer=test_customer,
            products=test_products,
            delivery_address=TEST_ADDRESS,
            delivery_date=TEST_DATE,
            order_total=(100.0 + 26.0) * 1.02
        )

        # Act
        result = service.create_response_object(
            test_customer, test_order, test_products)

        # Assert
        self.assertEqual(expected, result)

    def test_update_returnsUpdatedOrder_whenQueryUpdatesSomething(self):
        with patch('services.order_service.update_query') as update_func:
            # Arrange
            update_func.return_value = 1

            new_date = date(5555, 5, 5)
            new_address = 'new address'
            test_order = create_order(10)
            test_update = OrderUpdate(
                delivery_date=new_date, delivery_address=new_address)

            # Act
            result = service.update(test_update, test_order)

            # Assert
            self.assertEqual(result.delivery_address, new_address)
            self.assertEqual(result.delivery_date, new_date)
            self.assertEqual(result.id, test_order.id)

    def test_update_returnsUpdatedOrder_whenQueryUpdatesNothing(self):
        with patch('services.order_service.update_query') as update_func:
            # Arrange
            update_func.return_value = 0
            test_update = OrderUpdate(
                delivery_date=date(5555, 5, 5),
                delivery_address='new address')

            # Act
            result = service.update(test_update, create_order(10))

            # Assert
            self.assertIsNone(result)
