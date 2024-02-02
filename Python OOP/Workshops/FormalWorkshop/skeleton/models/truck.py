from models.vehicle import Vehicle
from core import validate


class Truck(Vehicle):
    WEIGHT_CAP_MIN = 1
    WEIGHT_CAP_MAX = 100
    WEIGHT_CAP_ERR = f'Weight capacity must be between {WEIGHT_CAP_MIN} and {WEIGHT_CAP_MAX}!'

    WHEELS_COUNT = 8

    def __init__(self, make, model, price, weight_capacity):
        self._weight_capacity = validate.intval(weight_capacity, Truck.WEIGHT_CAP_MIN, Truck.WEIGHT_CAP_MAX,
                                                Truck.WEIGHT_CAP_ERR)
        super().__init__(make, model, price)

    @property
    def weight_capacity(self):
        return self._weight_capacity

    def __str__(self):
        res = super().__str__()
        res.append(f'Weight Capacity: {self.weight_capacity}t')
        if not self.comments:
            comments_msg = ['--NO COMMENTS--']
        else:
            comments_msg = ['--COMMENTS--', ]
            for c in self.comments:
                comments_msg.append(str(c))
            comments_msg.append('--COMMENTS--')

        res.extend(comments_msg)
        return '\n'.join(res)
