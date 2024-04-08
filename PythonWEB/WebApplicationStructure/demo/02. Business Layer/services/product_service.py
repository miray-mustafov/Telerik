from data import Product, products


def all(search: str = None):
    if search is None:
        return products
    else:
        return [p for p in products if (search.lower() in p.name.lower())]


def get_by_id(id: int):
    return next((p for p in products if p.id == id), None)


def get_by_category(category_id: int):
    return list(filter(lambda p: p.category_id == category_id, products))


def sort(products: list[Product], *, attribute='price', reverse=False):
    if attribute == 'price':
        def sort_fn(p: Product): return p.price
    elif attribute == 'name':
        def sort_fn(p: Product): return p.name
    else:
        def sort_fn(p: Product): return p.id

    return sorted(products, key=sort_fn, reverse=reverse)


def create(product: Product):
    max_id = max(p.id for p in products)

    product.id = max_id + 1
    products.append(product)

    return product


def update(old: Product, new: Product):
    old.name = new.name
    old.description = new.description
    old.price = new.price
    old.category_id = new.category_id

    return old
