import os

from commands.base.base_command import BaseCommand


class AppendTextCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 3)

    def execute(self):
        directory_name, file_name, *text = self._params
        directory_path = os.path.join(self.demo_folder_path, directory_name)
        file_path = os.path.join(directory_path, file_name)

        if not os.path.exists(directory_path):
            return f'Directory {directory_name} does not exist.'

        if not os.path.exists(file_path):
            return f'File {file_name} does not exist.'

        with open(file_path, 'a') as file:
            file.write('\n' + ' '.join(text))
        return f'New line appended to file {file_name}'
