from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_int, validate_params_count, try_parse_float
from models.usage_type import UsageType


class CreateShampooCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 6)
        self._params = params
        self._app_data = app_data

    def execute(self):
        name, brand, price, gender, milliliters, usage_type = self._params
        if (usage_type[0] == '-' and usage_type[1:].isdigit()) or usage_type.isdigit():
            milliliters, usage_type = usage_type, milliliters
        gender = Gender.from_string(gender)
        usage_type = UsageType.from_string(usage_type)
        price = try_parse_float(price)
        milliliters = try_parse_int(milliliters)

        if self._app_data.product_exists(name):
            raise ValueError(f"Product {name} already exists!")
        self._app_data.create_shampoo(name, brand, price, gender, milliliters, usage_type)

        return f'Shampoo with name {name} was created!'
