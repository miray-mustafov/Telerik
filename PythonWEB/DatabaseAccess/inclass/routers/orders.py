from fastapi import APIRouter, Response
from data.models import Order
from services import order_service
from services import product_service

orders_router = APIRouter(prefix='/orders')


@orders_router.get('/')
def get_orders(sort: str | None = None):
    orders = order_service.all()

    if sort and (sort == 'asc' or sort == 'desc'):
        return order_service.sort(orders, reverse=sort == 'desc')

    return orders


@orders_router.get('/{id}')
def get_order_by_id(id: int):
    order, products = order_service.get_by_id(id)

    if order is None:
        return Response(status_code=404)

    return order_service.create_response_object(order, products)


@orders_router.post('/')
def create_order(order: Order):
    if order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    if not all(product_service.exists(id) for id in order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    order = order_service.create(order)

    return order


@orders_router.put('/{id}')
def update_order(id: int, new_order: Order):
    if new_order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    if not all(product_service.exists(id) for id in new_order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    existing_order, _ = order_service.get_by_id(id)
    if not existing_order:
        return Response(status_code=404)

    existing_order, products = order_service.update(existing_order, new_order)

    return order_service.create_response_object(existing_order, products)


@orders_router.delete('/{id}')
def delete_order(id: int):
    if not order_service.exists(id):
        return Response(status_code=404)

    order_service.delete(id)
    return Response(status_code=204)
