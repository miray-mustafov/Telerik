from data.database import read_query
from data.models import Product


def get_all():
    pass


def get_by_id(id: int):
    data = read_query(
        'SELECT id,name,price,category_id FROM products WHERE id = ?'
        , (id,)
    )
    if data:
        return Product.from_query_result(*data[0])
