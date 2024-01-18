class Product:
    def __init__(self, name, brand, price, gender):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()

    @name.setter
    def name(self, value):
        raise NotImplementedError()

    @property
    def brand(self):
        raise NotImplementedError()

    @brand.setter
    def brand(self, value):
        raise NotImplementedError()

    @property
    def price(self):
        raise NotImplementedError()

    @price.setter
    def price(self, value):
        raise NotImplementedError()

    @property
    def gender(self):
        raise NotImplementedError()

    def to_string(self):
        raise NotImplementedError()
