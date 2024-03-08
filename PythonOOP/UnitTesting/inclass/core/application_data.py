from models.category import Category
from models.gender import Gender
from models.product import Product


class ApplicationData:
    def __init__(self):
        self._products: list[Product] = []
        self._categories: list[Category] = []

    @property
    def products(self):
        return tuple(self._products)

    @property
    def categories(self):
        return tuple(self._categories)

    def find_product_by_name(self, name: str) -> Product:
        for product in self._products:
            if product.name == name:
                return product

        raise ValueError(f'Product {name} does not exist.')

    def find_category_by_name(self, name: str) -> Category:
        for category in self._categories:
            if category.name == name:
                return category

        raise ValueError(f'Category {name} does not exist.')

    def create_category(self, name: str) -> None:
        if self.category_exists(name):
            raise ValueError(f'Category {name} already exists!')

        category = Category(name)
        self._categories.append(category)

    def create_product(self, name: str, brand: str, price: float, gender: Gender) -> None:
        if self.product_exists(name):
            raise ValueError(f'Product {name} already exists!')

        product = Product(name, brand, price, gender)
        self._products.append(product)

    def category_exists(self, name: str) -> bool:
        return name in [c.name for c in self._categories]

    def product_exists(self, name: str) -> bool:
        return name in [p.name for p in self._products]
