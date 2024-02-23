class InvalidParams(Exception):
    def __init__(self, cmd_name, count):
        super().__init__(f'{cmd_name} command expects {count} parameters.')
