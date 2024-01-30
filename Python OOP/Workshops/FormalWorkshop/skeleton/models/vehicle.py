from core import validate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.comment import Comment


class Vehicle:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    def __init__(self, make, model, price):
        self._make = validate.str_len(make, Vehicle.MAKE_LEN_MIN, Vehicle.MAKE_LEN_MAX, Vehicle.MAKE_LEN_ERR)
        self._model = validate.str_len(model, Vehicle.MODEL_LEN_MIN, Vehicle.MODEL_LEN_MAX, Vehicle.MODEL_LEN_ERR)
        self._price = validate.intval(price, Vehicle.PRICE_MIN, Vehicle.PRICE_MAX, Vehicle.PRICE_ERR)
        self._comments: list['Comment'] = []

    @property
    def wheels(self):
        return type(self).WHEELS_COUNT

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def price(self):
        return self._price

    @property
    def comments(self):
        return tuple(self._comments)

    def add_comment(self, comment: 'Comment'):
        self._comments.append(comment)

    def get_comment(self, index):  # searches by indx
        if index >= len(self._comments):
            raise ValueError('Invalid index!')
        return self._comments[index]

    def remove_comment(self, comment: 'Comment'):
        if comment in self._comments:
            self._comments.remove(comment)

    def __str__(self):
        raise NotImplementedError('must be overriden')
