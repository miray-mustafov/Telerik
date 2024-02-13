
from commands.base.base_command import BaseCommand


class AppendTextCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 3)

    def execute(self):
        raise NotImplementedError()
