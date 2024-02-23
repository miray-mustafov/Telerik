from commands.base.base_command import BaseCommand
import os

class CountFilesCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 0)

    def execute(self):
        demo_folder_path = self.demo_folder_path

        files_count = sum(len(files) for _, _, files in os.walk(demo_folder_path))
        return f"Total files in demo_folder: {files_count}"