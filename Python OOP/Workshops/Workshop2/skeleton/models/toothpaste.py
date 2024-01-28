from models.product import Product


class Toothpaste(Product):
    def __init__(self, name, brand, price, gender, ingredients):
        super().__init__(name, brand, price, gender)
        self._ingredients = ingredients

    @property
    def ingredients(self):
        return tuple(self._ingredients)

    def to_string(self):
        res = super().to_string()
        display_ingredients = ', '.join(self.ingredients)
        res += f'\n #Ingredients: [{display_ingredients}]'
        return res
