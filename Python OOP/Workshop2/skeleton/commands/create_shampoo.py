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
        raise NotImplementedError()
