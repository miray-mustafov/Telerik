from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_int, validate_params_count, try_parse_float

from models.scent import Scent


class CreateCreamCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        name, brand, price, gender, scent = self._params
        price = try_parse_float(price)
        gender = Gender.from_string(gender)
        scent = Scent.check_scent(scent)

        if self._app_data.product_exists(name):
            raise ValueError(f"Cream {name} already exists!")
        self._app_data.create_cream(name, brand, price, gender, scent)

        return f'Cream with name {name} was created!'
