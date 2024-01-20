class Product:
    def __init__(self, name, brand, price, gender):
        self.name = name
        self.brand = brand
        self.price = price
        self._gender = gender  # validated from commands

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not 3 <= len(value) <= 10:
            raise ValueError('Minimum product name’s length is 3 symbols and maximum is 10 symbols!')
        self._name = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not 2 <= len(value) <= 10:
            raise ValueError('Minimum brand name’s length is 2 symbols and maximum is 10 symbols!')
        self._brand = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative!')
        self._price = value

    @property
    def gender(self):
        return self._gender

    def to_string(self):
        return f' #{self.name} {self.brand}\n #Price: ${self.price:.2f}\n #Gender: {self.gender}'

    # def __repr__(self):
    #     return f'{self.brand} {self.name} {self.price}$'
