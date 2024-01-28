from models.product import Product
from models.scent import Scent


class Cream(Product):
    def __init__(self, name, brand, price, gender, scent):
        super().__init__(name, brand, price, gender)
        self._scent = Scent.check_scent(scent)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not 3 <= len(value) <= 15:
            raise ValueError('Cream\'s name length must be between 3 and 15!')
        self._name = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not 3 <= len(value) <= 15:
            raise ValueError('Cream\'s brand length must be between 3 and 15!')
        self._brand = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not value > 0:
            raise ValueError('Cream\'s price must be > 0!')
        self._price = value

    @property
    def scent(self):
        return self._scent

    def to_string(self):
        return super().to_string() + f'\n #Scent: {self.scent}'

# nivea = Cream('SunBeauty', 'Nivea', 10.98, 'Women', 'lavender')
# print(nivea.name)
# print(nivea.to_string())
