from commands.base.base_command import BaseCommand


class CreateDirectoryCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 1)

    def execute(self):
       raise NotImplementedError()