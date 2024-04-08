from data import Category, categories


def all():
    return categories


def get_by_id(id: int):
    return next((c for c in categories if c.id == id), None)


def exists(id: int):
    return any(c.id == id for c in categories)


def create(category: Category):
    max_id = max(c.id for c in categories)

    category.id = max_id + 1
    categories.append(category)

    return category
