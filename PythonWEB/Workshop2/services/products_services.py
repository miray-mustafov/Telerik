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


def _get_top3_category_interests(categories_interests):
    res = list(sorted(categories_interests, key=lambda x: -x[-1]))
    res = [c[0] for c in res]
    return res[:3]


def get_random_product_by_categories(categories_interests: list[str] | None):
    cat_filter = ' '
    if categories_interests:
        top3 = _get_top3_category_interests(categories_interests)
        cat_filter = f' WHERE category_id IN {tuple(top3)} '

    query = f'SELECT id,name,price, category_id FROM products{cat_filter}ORDER BY RANDOM() LIMIT 1'

    data = read_query(query)
    if data:
        return Product.from_query_result(*data[0])
