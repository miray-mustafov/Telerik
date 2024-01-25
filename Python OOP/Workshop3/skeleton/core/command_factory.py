from core.application_data import ApplicationData
from commands.derived.add_test import AddTestCommand
from commands.derived.add_testgroup import AddTestGroupCommand


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == 'addtestgroup':
            return AddTestGroupCommand(params, self._app_data)
        if cmd.lower() == 'addtest':
            return AddTestCommand(params, self._app_data)
        # if cmd.lower() == "createcategory":
        #     return CreateCategoryCommand(params, self._app_data)

        raise ValueError(f'Invalid command: {cmd}')
