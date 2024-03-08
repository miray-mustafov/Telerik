from commands.base.base_command import BaseCommand
import os


class CountLinesCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 0)

    def execute(self):
        demo_folder_path = self.demo_folder_path

        total_lines = 0
        for root, _, files in os.walk(demo_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    total_lines += sum(1 for _ in f)
        return f"Total lines in all files in demo_folder: {total_lines}"
