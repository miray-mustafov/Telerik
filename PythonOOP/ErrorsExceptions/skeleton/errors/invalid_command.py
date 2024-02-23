class InvalidCommand(Exception):
    def __init__(self, cmd_name):
        super().__init__(f'Command {cmd_name} is not supported.')
