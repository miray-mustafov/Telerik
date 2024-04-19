import requests
from config import BASE_URL

USERS_URL = f'{BASE_URL}/users'


def login():
    username = input('Username = ')
    password = input('Password = ')
    response = requests.post(f"{USERS_URL}/login", json={'name': username, 'password': password})
    # todo


def register():
    username = input('Username = ')
    password = input('Password = ')
    # role = input('Role = ')

    response = requests.post(f"{USERS_URL}/register", json={'name': username, 'password': password})

    print(response)
    print(response.json())
    # if response.status_code == 200:  # Created
    #     id = response.json()['user']['id']
    #     print(f'Created category with id {id}')
    # if response.status_code == 400:
    #     print(response.text)
    # if response.status_code == 422:
    #     print('Invalid model schema:')
    #     errors = response.json()['detail']
    #     for error in errors:
    #         print('-', error['msg'], '->', error['loc'][1])


def get_info_by_id():
    category_id = int(input('Category id = '))
    response = requests.get(f'{USERS_URL}/{category_id}')
    data = response.json()

    category = data['category']
    products = data['products']

    print(f'==== {category["name"]} ====')
    for product in products:
        print(product)


def logout():
    pass


def select_action(cur_token):
    if not cur_token:
        actions = {
            'login': login,
            'register': register,
        }
    else:
        actions = {
            'logout': login,
            'info': register,
        }

    print('Select user action?')
    print(' / '.join(actions.keys()))

    actions[input().lower()]()
    a = 2
