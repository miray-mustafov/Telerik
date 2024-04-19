import requests
from commands.action import Action
from config import BASE_URL
from views import product_response_view

PRODUCTS_URL = f'{BASE_URL}/products'


def show_all():
    response = requests.get(f'{PRODUCTS_URL}')

    if response.status_code == 200:
        [print(el) for el in response.json()]
        # print(response.json())
    else:
        print(response.text)


def single():
    product_id = int(input('Products id = '))
    response = requests.get(f'{PRODUCTS_URL}/{product_id}')

    if response.status_code == 200:
        print(product_response_view(response.json()))
    elif response.status_code == 404:
        print('Product not found')
    else:
        print(response.text)


def create(token):
    name = input('name = ')
    description = input('description = ')
    price = input('price = ')
    category_id = input('category_id = ')

    data = {
        'name': name,
        'description': description,
        'price': price,
        'category_id': category_id,
    }

    response = requests.post(f'{PRODUCTS_URL}',
                             headers={'x-token': token},
                             json=data)

    if response.status_code == 200:
        print(product_response_view(response.json()))
    else:
        print(response.text)


def update(token):
    product_id = int(input('Product id to update = '))
    name = input('name = ')

    description = input('description = ')
    price = input('price = ')
    category_id = input('category_id = ')

    data = {
        'name': name,
        'description': description,
        'price': price,
        'category_id': category_id,
    }

    response = requests.put(f'{PRODUCTS_URL}/{product_id}',
                            headers={'x-token': token},
                            json=data)

    if response.status_code == 200:
        print('Successfully updated.')
    else:
        print(response.text)


def delete(token):
    product_id = int(input('Product id to delete = '))
    response = requests.delete(f'{PRODUCTS_URL}/{product_id}',
                               headers={'x-token': token})

    if response.status_code == 204:
        print('Successfully deleted.')
    else:
        print(response.text)


def select_action():
    actions = {
        'A': Action(show_all, requires_login=False, name='[A]ll'),
        'S': Action(single, requires_login=False, name='[S]ingle'),
        'C': Action(create, requires_login=True, name='[C]reate'),
        'U': Action(update, requires_login=True, name='[U]pdate'),
        'D': Action(delete, requires_login=True, name='[D]elete'),
    }

    print('Select products action?')
    print(' / '.join(action.name for action in actions.values()))

    selected_action = input().upper()
    actions.get(selected_action, Action.default()).execute()
