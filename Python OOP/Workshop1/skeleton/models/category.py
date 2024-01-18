class Category:
    def __init__(self, name):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()

    @name.setter
    def name(self, value):
        raise NotImplementedError()

    @property
    def products(self):
        raise NotImplementedError()

    def add_product(self, product):
        raise NotImplementedError()

    def remove_product(self, product):
        raise NotImplementedError()

    def to_string(self):
        raise NotImplementedError()
