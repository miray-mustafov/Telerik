from data import Order, orders, products


def has_missing_product_ids(ordered_product_ids: list[int]):
    valid_product_ids = [p.id for p in products]
    return any((id not in valid_product_ids) for id in ordered_product_ids)


def order_or_none(id: int):
    return next((i for i in orders if i.id == id), None)


def create_order_response(order: Order):
    FREE_SHIPPING_LIMIT = 125.0
    SHIPPING_FEE = 1.02
    order_products = [next(i for i in products if i.id == id) for id in order.product_ids]
    order_total = sum(p.price for p in order_products)
    if order_total > FREE_SHIPPING_LIMIT:
        order_total = order_total * SHIPPING_FEE

    return {
        'id': order.id,
        'customer': order.customer,
        'products': order_products,
        'delivery_date': order.delivery_date,
        'order_total': order_total
    }
