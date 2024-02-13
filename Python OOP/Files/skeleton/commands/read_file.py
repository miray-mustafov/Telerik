from commands.base.base_command import BaseCommand
import os


class ReadFileCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 2)

    def execute(self):
        directory_name, file_name = self._params
        directory_path = os.path.join(self.demo_folder_path, directory_name)
        file_path = os.path.join(directory_path, file_name)

        if not os.path.exists(directory_path):
            return f"Directory '{directory_name}' does not exist."

        if not os.path.exists(file_path):
            return f"File '{file_name}' does not exist."

        with open(file_path, 'r') as file:
            content = file.readlines()
            if not content:
                return f"{file_name} contents:\n (empty)"
            formatted_content = ''.join([f" {i + 1}. {line}" for i, line in enumerate(content)])
            return f"{file_name} contents:\n{formatted_content}"
