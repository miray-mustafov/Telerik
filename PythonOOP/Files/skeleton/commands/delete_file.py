from commands.base.base_command import BaseCommand
import os


class DeleteFileCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 2)

    def execute(self):
        directory_name, file_name = self._params
        directory_path = os.path.join(self.demo_folder_path, directory_name)
        file_path = os.path.join(directory_path, file_name)

        if not os.path.exists(directory_path):
            return f"Directory {directory_name} does not exist."

        if not os.path.exists(file_path):
            return f"File {file_name} does not exist."

        os.remove(file_path)
        return f"File '{file_name}' deleted from directory '{directory_name}'."
