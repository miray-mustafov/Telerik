from fastapi import FastAPI
from data import Product, products

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
    return products


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


