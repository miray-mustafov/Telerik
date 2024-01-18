from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


class ApplicationData:
    def __init__(self):
        raise NotImplementedError()

    @property
    def products(self):
        raise NotImplementedError()

    @property
    def categories(self):
        raise NotImplementedError()

    @property
    def shopping_cart(self) -> ShoppingCart:
        raise NotImplementedError()

    def find_product_by_name(self, name) -> Product:
        raise NotImplementedError()

    def find_category_by_name(self, name) -> Category:
        raise NotImplementedError()

    def create_category(self, name) -> None:
        raise NotImplementedError()

    def create_product(self, name, brand, price, gender) -> None:
        raise NotImplementedError()

    def category_exists(self, name) -> bool:
        raise NotImplementedError()

    def product_exists(self, name) -> bool:
        raise NotImplementedError()
