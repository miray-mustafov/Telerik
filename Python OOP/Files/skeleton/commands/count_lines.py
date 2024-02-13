
from commands.base.base_command import BaseCommand


class CountLinesCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 0)

    def execute(self):
       raise NotImplementedError()
