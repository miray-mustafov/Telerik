from commands.base.base_command import BaseCommand
import os


class CreateDirectoryCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 1)

    def execute(self):
        directory_name = self._params[0]
        directory_path = os.path.join(self.demo_folder_path, directory_name)

        try:
            os.makedirs(directory_path)
            return f"Directory {directory_name} created."
        except FileExistsError:
            return f"Directory {directory_name} already exists."
