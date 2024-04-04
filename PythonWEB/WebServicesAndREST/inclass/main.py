import uvicorn
from fastapi import FastAPI, Response
from data import Product, Order, products, orders, extended_order_info

app = FastAPI()


# if __name__ == "__main__":
#     uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)

@app.get('/')
def root():
    return 'Hello!'


@app.get('/products')
def get_products(
        sort: str | None = None,
        search: str | None = None,
):
    result = list(products.values())

    if search:
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')

    return result


@app.get('/products/{id}')
def get_product_by_id(id: int):
    product = next((p for p in products.values() if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        return product


@app.post('/products', status_code=201)
def create_product(product: Product):
    max_id = max(n for n in products)

    product.id = max_id + 1
    products[product.id] = product

    return product


@app.put('/products/{id}')
def update_product(id: int, product: Product):
    existing_product = products.get(id, None)

    if existing_product is None:
        return Response(status_code=404)

    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price

    return existing_product


# ---------------------ORDERS--------------------------------
@app.get('/orders')
def get_orders(
        sort: str | None = None,
        search: str | None = None,
):
    # sorts by delivery_date
    # searches by customer

    cur_orders = list(orders.values())
    if search:
        cur_orders = [o for o in cur_orders if search.lower() in o.customer.lower()]
    if sort == 'asc' or sort == 'desc':
        cur_orders = sorted(cur_orders, key=lambda p: p.delivery_date, reverse=sort == 'desc')
    return cur_orders


@app.get('/orders/{id}')
def get_order_by_id(id: int):
    order: Order = orders.get(id, None)

    if order is None:
        return Response(status_code=404)
    info: dict = extended_order_info(order)
    return info


@app.post('/orders', status_code=201)
def create_order(order: Order):
    for pid in order.product_ids:
        if pid not in products:
            return Response('Must contain existing products', status_code=400)

    max_id = max(num for num in orders.keys())
    order.id = max_id + 1
    orders[order.id] = order

    return order


@app.put('/orders/{id}')
def update_order(id: int, order: Order):
    existing_order = orders.get(id, None)

    if existing_order is None:
        return Response('NOT FOUND', status_code=404)
    for pid in order.product_ids:
        if pid not in products:
            return Response('Must contain existing products', status_code=400)

    existing_order.customer = order.customer
    existing_order.product_ids = order.product_ids
    existing_order.delivery_date = order.delivery_date

    return extended_order_info(existing_order)


@app.delete('/orders/{id}', status_code=204)
def delete_order(id: int):
    if id not in orders:
        return Response('NOT FOUND', status_code=404)
    orders.pop(id)
    return f"Order with id {id} deleted!"
