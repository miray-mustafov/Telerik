
from core.application_data import ApplicationData


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):

        raise NotImplementedError()
