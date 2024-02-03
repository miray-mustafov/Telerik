from models.gender import Gender


class Product:
    def __init__(self, name: str, brand: str, price: float, gender: Gender):
        self.name = name
        self.brand = brand
        self.price = price
        self._gender = Gender(gender)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) < 3 or len(value) > 10:
            raise ValueError('Name should be between 3 and 10 symbols.')

        self._name = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if len(value) < 2 or len(value) > 10:
            raise ValueError(
                'Product brand should be between 2 and 10 symbols.')

        self._brand = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError('Price can\'t be negative')

        self._price = value

    @property
    def gender(self):
        return self._gender.value

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender.value}',
            ' ==='
        ])



