from fastapi import FastAPI
from data import Product, data

app = FastAPI()


@app.get('/')
def root():
    return {
        'description': 'Product API',
        'routes': [
            ('GET', '/products', 'List of products')
        ]
    }


# @app.get('/products')
# def get_products():
#     return data


@app.get('/products')
def get_product_by_id(search: str = None):
    if search:
        products = [p for p in data if p.name.lower() == search.lower()]
        if not products:
            return data
        return products
    return data


@app.get('/products/{id}')
def get_product_by_id(id: int):
    prod = [p for p in data if p.id == id]
    if not prod:
        return "No such product"
    return prod[0]


@app.post('/products', status_code=201)
def create_product(product: Product):
    max_id = max(p.id for p in data)
    product.id = max_id + 1
    data.append(product)
    return product


@app.put('/products/{id}', status_code=202)  # Accepted
def update_prod_by_id(id: int, product: Product):
    product_to_update = [p for p in data if p.id == id]
    product_to_update = product_to_update[0]
    if product:
        product_to_update.name = product.name
        product_to_update.description = product.description
        product_to_update.price = product.price
    return product_to_update


@app.delete('/products/{id}')
def delete_prod_by_id(id: int):
    prod = [p for p in data if p.id == id]
    if not prod:
        return "No such product"
    data.remove(prod[0])
    return f"Prod with id {id} deleted!"
