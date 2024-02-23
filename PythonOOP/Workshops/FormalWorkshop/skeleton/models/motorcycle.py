from models.vehicle import Vehicle
from core import validate


class Motorcycle(Vehicle):
    CATEGORY_LEN_MIN = 3
    CATEGORY_LEN_MAX = 10
    CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'

    WHEELS_COUNT = 2

    def __init__(self, make, model, price, category):
        self._category = validate.str_len(category, Motorcycle.CATEGORY_LEN_MIN, Motorcycle.CATEGORY_LEN_MAX,
                                          Motorcycle.CATEGORY_LEN_ERR)
        super().__init__(make, model, price)

    @property
    def category(self):
        return self._category

    def __str__(self):
        res = super().__str__()
        res.append(f'Category: {self.category}')
        if not self.comments:
            comments_msg = ['--NO COMMENTS--']
        else:
            comments_msg = ['--COMMENTS--', ]
            for c in self.comments:
                comments_msg.append(str(c))
            comments_msg.append('--COMMENTS--')

        res.extend(comments_msg)
        return '\n'.join(res)
