import os


class BaseCommand:
    def __init__(self, params, expected):
        if len(params) < expected:
            raise ValueError(
                f'{type(self).__name__} expected at least {expected} arguments, only {len(params)} given.')
        self._params = params
        self._demo_folder_path = os.path.join(
            os.path.dirname(__file__), '../../demo_folder')

    @property
    def demo_folder_path(self):
        return self._demo_folder_path

    def execute(self):
        # override in derived classes
        return ''
