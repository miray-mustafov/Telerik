from fastapi import APIRouter, Response
from data import Product, products, categories


product_router = APIRouter(prefix='/products')


@product_router.get('/')
def get_products(
    sort: str | None = None,
    search: str | None = None
):
    result = products

    if search:
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')

    return result


@product_router.get('/{id}') 
def get_product_by_id(id: int):
    product = next((p for p in products if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        return product


@product_router.post('/', status_code=201)
def create_product(product: Product):
    if not any(c.id == product.category_id for c in categories):
        return Response(status_code=400,
                        content=f'Category {product.category_id} does not exist')

    max_id = max(p.id for p in products)

    product.id = max_id + 1
    products.append(product)

    return product


@product_router.put('/{id}')
def update_product(id: int, product: Product):
    if not any(c.id == product.category_id for c in categories):
        return Response(status_code=400,
                        content=f'Category {product.category_id} does not exist')

    existing_product = next((p for p in products if p.id == id), None)
    if existing_product is None:
        return Response(status_code=404)
    else:
        existing_product.name = product.name
        existing_product.description = product.description
        existing_product.price = product.price
        existing_product.category_id = product.category_id

        return existing_product
