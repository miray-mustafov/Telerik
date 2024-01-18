class ShoppingCart:
    def __init__(self):
        raise NotImplementedError()

    @property
    def products(self):
        raise NotImplementedError()

    def add_product(self, product):
        raise NotImplementedError()

    def remove_product(self, product):
        raise NotImplementedError()

    def contains_product(self, product):
        raise NotImplementedError()

    def total_price(self):
        raise NotImplementedError()
