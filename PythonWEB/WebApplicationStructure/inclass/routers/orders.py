from fastapi import APIRouter, Response
from data import Order
from services import order_service
from data import orders

orders_router = APIRouter(prefix='/orders')


@orders_router.get('/')
def get_orders(sort: str | None = None):
    if sort and (sort == 'asc' or sort == 'desc'):
        return sorted(orders, key=lambda p: p.delivery_date, reverse=sort == 'desc')

    return orders


@orders_router.get('/{id}')
def get_order_by_id(id: int):
    order = order_service.order_or_none(id)

    if order is None:
        return Response(status_code=404)
    else:
        return order_service.create_order_response(order)


@orders_router.post('/')
def create_order(order: Order):
    if order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    if order_service.has_missing_product_ids(order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    order.id = max(o.id for o in orders) + 1
    orders.append(order)

    return order_service.create_order_response(order)


@orders_router.put('/{id}')
def update_order(id: int, order: Order):
    existing_order = order_service.order_or_none(id)

    if existing_order is None:
        return Response(status_code=404)

    if order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    if order_service.has_missing_product_ids(order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    existing_order.product_ids = order.product_ids
    existing_order.delivery_date = order.delivery_date

    return order_service.create_order_response(existing_order)


@orders_router.delete('/{id}')
def delete_order(id: int):
    existing_order = order_service.order_or_none(id)

    if existing_order is None:
        return Response(status_code=404)

    orders.remove(existing_order)

    return Response(status_code=204)
