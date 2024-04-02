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


@app.get('/products')
def get_products():
    ids = []
    product: Product = None
    for product in data:
        ids.append(product.id)

    return ids
