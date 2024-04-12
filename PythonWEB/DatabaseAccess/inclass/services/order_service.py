from data.models import Order
from services import product_service
from data.database import insert_query, read_query, update_query
from data.models import Product


def exists(id: int):
    return any(
        read_query(
            'select id from orders where id = ?',
            (id,))
    )


def sort(lst: list[Order], reverse=False):
    return sorted(
        lst,
        key=lambda p: p.delivery_date,
        reverse=reverse)


def orders_dict(data: list):
    orders = {}
    for id, customer, pid, odate in data:
        if id not in orders:
            orders[id] = Order.from_query_result(id, customer, [], odate)
        orders[id].product_ids.append(pid)
    return orders


def orders_list(orders_dict: dict):
    orders_list = []
    for obj in orders_dict.values():
        orders_list.append(obj)
    return orders_list


def all():
    data = read_query(
        '''SELECT o.id, o.customer, op.products_id, o.delivery_date
        FROM orders o join orders_has_products op on o.id = op.orders_id''')

    orders = orders_dict(data)
    orders = orders_list(orders)

    return orders


def get_by_id(id: int):
    data = read_query(
        '''SELECT o.id, o.customer, op.products_id, o.delivery_date
        FROM orders o join orders_has_products op on o.id = op.orders_id
        where o.id = ?''', (id,))

    orders_products = read_query(
        '''SELECT p.id, p.name, p.description, p.price, p.category_id
            FROM products p JOIN orders_has_products op ON p.id = op.products_id 
            WHERE op.orders_id = ?''', (id,)
    )

    order = orders_dict(data)
    order = order[id]

    return order, orders_products


def create_response_object(order, products_tuple):
    FREE_SHIPPING_LIMIT = 125.0
    SHIPPING_FEE = 1.02
    products = [Product.from_query_result(*row) for row in products_tuple]

    order_total = sum(p.price for p in products)
    if order_total > FREE_SHIPPING_LIMIT:
        order_total = order_total * SHIPPING_FEE

    return {
        'id': order.id,
        'customer': order.customer,
        'products': products,
        'delivery_date': order.delivery_date,
        'order_total': order_total
    }


def create(order: Order):
    order_id = insert_query(
        'INSERT INTO orders(customer,delivery_date) VALUES(?,?)',
        (order.customer, order.delivery_date))

    # todo
    for product_id in order.product_ids:
        insert_query(
            'INSERT INTO orders_has_products(orders_id,products_id) VALUES(?,?)',
            (order_id, product_id))

    # order.id = generated_id
    return f'Order {order_id} was successfully created!!'


def update(old: Order, new: Order):
    old_ids = set(old.product_ids)
    new_ids = set(new.product_ids)
    to_delete = []
    to_add = []

    for id in new_ids:
        if id not in old_ids:
            to_add.append(id)

    for id in old_ids:
        if id not in new_ids:
            to_delete.append(id)

    for pid in to_delete:
        update_query(
            '''DELETE FROM orders_has_products WHERE orders_id = ? and products_id = ?''', (old.id, pid)
        )
    for pid in to_add:
        insert_query(
            'INSERT INTO orders_has_products(orders_id,products_id) VALUES(?,?)',
            (old.id, pid))

    update_query(
        '''UPDATE orders SET customer=?, delivery_date=? WHERE id = ?''',
        (new.customer, new.delivery_date, old.id)
    )

    orders_products = read_query(
        '''SELECT p.id, p.name, p.description, p.price, p.category_id
            FROM products p JOIN orders_has_products op ON p.id = op.products_id 
            WHERE op.orders_id = ?''', (old.id,)  # updated
    )
    return new, orders_products


def delete(id: int):
    update_query(
        '''DELETE FROM orders_has_products WHERE orders_id = ?''', (id,)
    )
    update_query(
        '''DELETE FROM orders WHERE id = ?''', (id,)
    )
