class Category:
    def __init__(self, name):
        self.name = name
        self._products = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not 2 <= len(value) <= 15:
            raise ValueError(f'Minimum category name’s length is 2 symbols and maximum is 15 symbols!')
        self._name = value

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product):
        if product in self._products:
            raise ValueError('Product already in the category!')
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)

    def to_string(self):
        res = f'#Category: {self.name}\n'
        if not self._products:
            res += ' #No products in this category'
        else:
            for i in range(len(self._products)):
                res += self._products[i].to_string() + '\n ===\n'
            res += self._products[-1].to_string()
        return res
