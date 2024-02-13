
from commands.base.base_command import BaseCommand


class DeleteFileCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 2)

    def execute(self):
       raise NotImplementedError()