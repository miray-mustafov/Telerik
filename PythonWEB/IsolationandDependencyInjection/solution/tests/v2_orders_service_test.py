import unittest
from datetime import date
from unittest.mock import Mock, patch
from data.models import Order
from services import order_service


class V2OrderService_Should(unittest.TestCase):
    pass

    # get by id - returns order
    def test_getById_returnsOrder(self):
        with patch('services.order_service.read_query') as read_query:
            read_query.return_value = [(1, '1989-02-07', 'Sofia', 1)]
            result = order_service.get_by_id(1)

        self.assertEqual(1, result.id)
        self.assertEqual(date(1989, 2, 7), result.delivery_date)


    # get by id - return none
    def test_getById_returnsNone(self):
        with patch('services.order_service.read_query') as read_query:
            read_query.return_value = []
            result = order_service.get_by_id(1)

        self.assertIsNone(result)

    # all - single order data is flattened [(order_id: 1, p_id: 1), (order_id: 1, p_id: 2)]
    def test_all_returnsSingleOrderData(self):
        with patch('services.order_service.read_query') as read_query:
            read_query.return_value = [
                (1, '1989-02-07', 'Sofia', 1, 4),
                (1, '1989-02-07', 'Sofia', 1, 5),
                (1, '1989-02-07', 'Sofia', 1, 6),
            ]
            result = list(order_service.all())

        first_order = result[0]
        
        self.assertEqual(1, len(result))
        self.assertEqual(1, first_order.id)
        self.assertEqual([4,5,6], sorted(first_order.product_ids))

    # all - order without products
    def test_all_returnsSingleOrderWithoutProductIds(self):
        with patch('services.order_service.read_query') as read_query:
            read_query.return_value = [(1, '1989-02-07', 'Sofia', 1, None)]
            result = list(order_service.all())

        first_order = result[0]
        
        self.assertEqual(1, len(result))
        self.assertEqual(1, first_order.id)
        self.assertEqual([], first_order.product_ids)
    
    # all - no data returned -> []
    def test_all_returnsEmptyList(self):
        with patch('services.order_service.read_query') as read_query:
            read_query.return_value = []
            result = list(order_service.all())
        
        self.assertEqual([], result)

    # all - multiple orders
    def test_all_returnsMultipleOrdersData(self):
        with patch('services.order_service.read_query') as read_query:
            read_query.return_value = [
                (1, '1989-02-07', 'Sofia', 1, 4),
                (1, '1989-02-07', 'Sofia', 1, 5),
                (2, '1989-02-07', 'Sofia', 1, 6),
                (3, '1989-02-07', 'Sofia', 1, 6),
                (3, '1989-02-07', 'Sofia', 1, 10),
                (3, '1989-02-07', 'Sofia', 1, 11),
                (4, '1989-02-07', 'Sofia', 1, None),
            ]
            result = list(order_service.all())

        first, second, third, fourth = result
        
        self.assertEqual(4, len(result))
        self.assertEqual([4,5], sorted(first.product_ids))
        self.assertEqual([6], sorted(second.product_ids))
        self.assertEqual([6,10,11], sorted(third.product_ids))
        self.assertEqual([], fourth.product_ids)

  

    # sort - reverse true 
    def test_sort_returnsInReverseOrder(self):
        A = Order(id = 1, delivery_date=date(1989, 2, 7), delivery_address='Sofia', user_id=1)
        B = Order(id = 1, delivery_date=date(1988, 2, 7), delivery_address='Sofia', user_id=1)
        C = Order(id = 1, delivery_date=date(1990, 2, 7), delivery_address='Sofia', user_id=1)
        D = Order(id = 1, delivery_date=date(1992, 2, 7), delivery_address='Sofia', user_id=1)

        result = order_service.sort([A, B, C, D], reverse=True)

        self.assertEqual([D, C, A, B], result)

    # sort - reverse false  
    def test_sort_returnsInOrder(self):
        A = Mock(delivery_date=date(1989, 2, 7))
        B = Mock(delivery_date=date(1988, 2, 7))
        C = Mock(delivery_date=date(1990, 2, 7))
        D = Mock(delivery_date=date(1992, 2, 7))

        result = order_service.sort([A, B, C, D], reverse=False)

        self.assertEqual([B, A, C, D], result)