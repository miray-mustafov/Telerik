from fastapi import FastAPI, Response
from data import data


app = FastAPI()

# example requests:
# /products
# /products?search=smart
# /products?search=tablet
# /products?search=smart&sort=desc
# /products?sort=desc&search=smart
# /products?sort=asc
# /products?sort=desc

@app.get('/products')
def get_products(
    sort=None,  # query param, optional
    search: str | None = None  # query param, optional
):
    result = data

    if search:
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')

    return result

# example requests:
# /products/1
# /products/2
# /products/{any int}

@app.get('/products/{id}')  # path parameter
def get_product_by_id(id: int):
    product = next((p for p in data if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        return product
