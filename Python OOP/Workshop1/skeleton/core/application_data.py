from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


class ApplicationData:
    def __init__(self):
        self._products = []
        self._categories = []
        self._shopping_cart = None  # todo

    @property
    def products(self):
        return self._products

    @property
    def categories(self):
        return self._categories

    @property
    def shopping_cart(self) -> ShoppingCart:
        return self._shopping_cart

    def find_product_by_name(self, name) -> Product:
        for product in self.products:
            if product.name == name:
                return product
        raise ValueError(f'Product {name} does\'nt exist')

    def find_category_by_name(self, name) -> Category:
        for category in self.categories:
            if category.name == name:
                return category
        raise ValueError(f'Category {name} does\'nt exist')

    def create_category(self, name) -> None:
        if self.category_exists(name):
            # raise ValueError(f'Category {name} already exists!')
            return  # todo
        self._categories.append(Category(name))

    def create_product(self, name, brand, price, gender) -> None:
        if self.product_exists(name):
            # raise ValueError(f'Product {name} already exists!')
            return
        self._products.append(Product(name, brand, price, gender))

    def category_exists(self, name) -> bool:
        return name in [x.name for x in self.categories]

    def product_exists(self, name) -> bool:
        return name in [x.name for x in self.products]
