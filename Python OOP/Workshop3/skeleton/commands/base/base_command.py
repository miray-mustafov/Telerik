from typing import List
from core.application_data import ApplicationData


class BaseCommand():
    def __init__(self, params: List[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    @property
    def params(self):
        return tuple(self._params)

    @property
    def app_data(self):
        return self._app_data

    def execute(self):
        return "must be overriden"
