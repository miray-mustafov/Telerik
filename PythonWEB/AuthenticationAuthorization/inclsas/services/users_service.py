from data.models import Order, User
from data.database import read_query
from services.order_service import get_orders_by_user_id

_SEPARATOR = ';'


def get_by_username(username: str) -> User | None:
    data = read_query(
        "SELECT id, username, password, role FROM users WHERE username = ?", (username,)
    )
    user = next((User.from_query_result(*row) for row in data), None)
    return user


def get_by_id(id: int) -> User | None:  # new
    data = read_query(
        "SELECT id, username, password, role FROM users WHERE id = ?", (id,)
    )
    user = next((User.from_query_result(*row) for row in data), None)
    return user


def get_by_id_and_username(id, username):
    data = read_query(
        "SELECT id, username, password, role FROM users WHERE id = ? and username = ?", (id, username,)
    )
    user = next((User.from_query_result(*row) for row in data), None)
    return user


def create_token(user: User) -> str:
    # note: this token is not particulary secure, use JWT for real-world uses
    return f'{user.id}{_SEPARATOR}{user.username}'


def is_authenticated(token: str) -> bool:
    # note: this token is not particulary secure, use JWT for real-world uses
    user_id, username = token.split(_SEPARATOR)

    # todo why get by id,username then  fromtoken > getby username
    user = get_by_id_and_username(int(user_id), username)
    return user is not None


def from_token(token: str) -> User | None:
    _, username = token.split(_SEPARATOR)

    return get_by_username(username)


def owns_order(user: User, order: Order) -> bool:  # mod
    return order.user_id == user.id

def add_orders_to_user(user: User):
    users_orders = get_orders_by_user_id(user.id)
    for order in users_orders:
        user.order_ids.append(order.id)