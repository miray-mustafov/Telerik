from data.in_memory_users import users
from data.models import Order, User

_SEPARATOR = ';'


def find_by_username(username: str) -> User | None:
    return next((u for u in users if u.username == username), None)


def create_token(user: User) -> str:
    # note: this token is not particulary secure, use JWT for real-world uses
    return f'{user.id}{_SEPARATOR}{user.username}'


def is_authenticated(token: str) -> bool:
    # note: this token is not particulary secure, use JWT for real-world uses
    user_id, username = token.split(_SEPARATOR)
    return any((u.id == int(user_id) and u.username == username)
               for u in users)


def from_token(token: str) -> User | None:
    _, username = token.split(_SEPARATOR)

    return find_by_username(username)


def owns_order(user: User, order: Order) -> bool:
    return order.id in user.orders
