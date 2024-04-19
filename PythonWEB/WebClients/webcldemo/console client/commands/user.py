import requests
from config import BASE_URL

USERS_URL = f'{BASE_URL}/users'


def get_info_by_id():
    category_id = int(input('Category id = '))
    response = requests.get(f'{USERS_URL}/{category_id}')
    data = response.json()

    category = data['category']
    products = data['products']

    print(f'==== {category["name"]} ====')
    for product in products:
        print(product)


def login():
    response = requests.get(USERS_URL)
    data = response.json()
    for object in data:
        category = object['category']
        products = object['products']

        print(
            f'{category["id"]}. {category["name"]} ({len(products)} products)')


def register():
    username = input('Username = ')
    password = input('Password = ')
    role = input('Role = ')  # todo remove and add user_update_role

    response = requests.post(USERS_URL, json={'name': username, 'password': password, 'role': role})

    #todo HERE, open the authentication solution, run server
    if response.status_code == 204:  # Created
        id = response.json()['category']['id']
        print(f'Created category with id {id}')
    if response.status_code == 400:
        print(response.text)
    if response.status_code == 422:
        print('Invalid model schema:')
        errors = response.json()['detail']
        for error in errors:
            print('-', error['msg'], '->', error['loc'][1])


def select_action():
    actions = {
        'login': login,
        'register': register,
        'info': get_info_by_id,
    }

    print('Select user action?')
    print(' / '.join(actions.keys()))

    actions[input().lower()]()
