from pydantic import BaseModel
from datetime import date


class Product(BaseModel):
    id: int | None = None
    name: str
    description: str
    price: float


class Order(BaseModel):
    id: int | None = None
    customer: str
    product_ids: list[int]
    delivery_date: date


products = {
    1: Product(id=1, name='TV', description='LCD 40 Inch', price=749.99),
    2: Product(id=2, name='Laptop', description='2x2.6 GHz CPU; 6GB RAM; HD Graphics', price=699.99),
    3: Product(id=3, name='Smartphone', description='6.55" HD+, 5G', price=1349.90),
    4: Product(id=4, name='Keyboard', description='Full-size Layout, Mechanical', price=99.00),
}

orders = {
    1: Order(
        id=1,
        customer='Steven',
        product_ids=[2, 4],
        delivery_date=date(2025, 2, 8)
    ),
    2: Order(
        id=2,
        customer='Alice',
        product_ids=[1],
        delivery_date=date(2023, 8, 4)
    ),
    3: Order(
        id=3,
        customer='Alice',
        product_ids=[3],
        delivery_date=date(2023, 8, 4)
    ),
}


def extended_order_info(order) -> dict:
    extended_order, cur_products, total = {}, [], 0

    for pid in order.product_ids:
        cur_products.append(products[pid])
        total += products[pid].price
    if total > 125:
        total *= 1.02

    extended_order['id'] = order.id
    extended_order['customer'] = order.customer
    extended_order['products'] = cur_products
    extended_order['delivery_date'] = order.delivery_date
    extended_order['order_total'] = total

    return extended_order
