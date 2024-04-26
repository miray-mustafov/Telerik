from data import database
from data.models import Category


def all(get_data_func = None):
    if get_data_func is None:
        get_data_func = database.read_query
        
    data = get_data_func('select id, name from categories order by id')

    return (Category(id=id, name=name) for id, name in data)


def get_by_id(id: int, get_data_func = None):
    if get_data_func is None:
        get_data_func = database.read_query

    data = get_data_func('select id, name from categories where id = ?', (id,))

    return next((Category(id=id, name=name) for id, name in data), None)


def exists(id: int, get_data_func = None):
    if get_data_func is None:
        get_data_func = database.read_query

    return any(
        get_data_func(
            'select id, name from categories where id = ?',
            (id,)))


def create(category: Category, insert_data_func = None):
    if insert_data_func is None:
        insert_data_func = database.insert_query

    generated_id = insert_data_func(
        'insert into categories(name) values(?)',
        (category.name,))

    category.id = generated_id

    return category
