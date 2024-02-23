from commands.base.base_command import BaseCommand
import os


class ListFilesCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 1)

    def execute(self):
        directory_name = self._params[0]
        directory_path = os.path.join(self.demo_folder_path, directory_name)

        if not os.path.exists(directory_path):
            return f"Error: Directory '{directory_name}' does not exist."

        files = os.listdir(directory_path)
        if not files:
            return f"No files found in directory '{directory_name}'."
        else:
            file_list = [f" {i + 1}. {file}" for i, file in enumerate(files)]
            return f"{directory_name} files:\n" + '\n'.join(file_list)
