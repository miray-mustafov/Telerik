from commands.add_to_category import AddToCategoryCommand
from commands.create_category import CreateCategoryCommand
from commands.create_product import CreateProductCommand
from commands.show_category import ShowCategoryCommand

from errors.invalid_command import InvalidCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line: str):
        cmd_name, *params = input_line.split()

        if cmd_name.lower() == "createcategory":
            return CreateCategoryCommand(params, self._app_data)
        if cmd_name.lower() == "createproduct":
            return CreateProductCommand(params, self._app_data)
        if cmd_name.lower() == "showcategory":
            return ShowCategoryCommand(params, self._app_data)
        if cmd_name.lower() == "addproducttocategory":
            return AddToCategoryCommand(params, self._app_data)

        raise InvalidCommand(cmd_name)
