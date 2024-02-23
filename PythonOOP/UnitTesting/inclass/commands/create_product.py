from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float


class CreateProductCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        validate_params_count(params, 4, 'CreateProduct')
        self._params = params
        self._app_data = app_data

    def execute(self):
        name, brand, price_str, gender_str = self._params
        price = try_parse_float(
            price_str, 'Third parameter should be price (real number).')
        gender = Gender(gender_str)

        if self._app_data.product_exists(name):
            raise ValueError(
                f'Product {name} already exists!')

        self._app_data.create_product(name, brand, price, gender)

        return f'Product with name {name} was created!'
