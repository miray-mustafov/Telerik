from models.product import Product


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, usage_type, milliliters):
        raise NotImplementedError()
