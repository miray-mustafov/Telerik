from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float


class CreateToothpasteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        name, brand, price, gender, ingredients = self._params
        if self._app_data.product_exists(name):
            raise ValueError(f"Product {name} already exists!")
        gender = Gender.from_string(gender)# todo Why needed here
        price = float(price)
        ingredients = tuple(ingredients.split(','))
        self._app_data.create_toothpaste(name, brand, price, gender, ingredients)

        return f'Toothpaste with name {name} was created!'
