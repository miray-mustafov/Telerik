from datetime import datetime


class EventLog:
    def __init__(self, description: str):
        if len(description) < 1:
            raise ValueError('Invalid description!')
        self._description = description
        self._timestamp = datetime.now()

    @property
    def description(self):
        return self._description

    @property
    def timestamp(self):
        return self._timestamp

    def info(self):
        return f'[{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}] {self.description}'
