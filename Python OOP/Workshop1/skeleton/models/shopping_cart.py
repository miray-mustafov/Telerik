class ShoppingCart:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        for i in range(len(self._products)):
            if self._products[i] == product:
                self._products.pop(i)
                return

    def contains_product(self, product):
        return product in self._products

    def total_price(self):
        return sum(x.price for x in self._products)
