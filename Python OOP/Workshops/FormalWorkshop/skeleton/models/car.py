from models.vehicle import Vehicle
from core import validate


class Car(Vehicle):
    CAR_SEATS_MIN = 1
    CAR_SEATS_MAX = 10
    CAR_SEATS_ERR = f'Seats must be between {CAR_SEATS_MIN} and {CAR_SEATS_MAX}!'

    WHEELS_COUNT = 4

    def __init__(self, make, model, price, seats):
        self._seats = validate.intval(seats, Car.CAR_SEATS_MIN, Car.CAR_SEATS_MAX, Car.CAR_SEATS_ERR)
        super().__init__(make, model, price)

    @property
    def seats(self):
        return self._seats

    def __str__(self):
        res = [
            'Car:',
            f'Make: {self.make}',
            f'Model: {self.model}',
            f'Wheels: {self.wheels}',
            f'Price: ${self.price:.2f}',
            f'Seats: {self.seats}',
        ]
        if not self.comments:
            comments_msg = ['--NO COMMENTS--']
        else:
            comments_msg = ['--COMMENTS--', ]
            for c in self.comments:
                comments_msg.append(str(c))
            comments_msg.append('--COMMENTS--')

        res.extend(comments_msg)
        return '\n'.join(res)
