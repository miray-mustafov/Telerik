from datetime import date
from item_status import ItemStatus


class BoardItem:
    def __init__(self, title: str, due_date: date):
        self.title = title
        self.due_date = due_date
        self._status = ItemStatus.OPEN

    @property
    def status(self):
        return self._status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) < 5 or len(value) > 30:
            raise ValueError('Illegal title length [5:30]')
        self._title = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if (value < date.today()):
            raise ValueError('Due date cant be in the past.')
        self._due_date = value

    def revert_status(self):
        self._status = ItemStatus.previous(self.status)

    def advance_status(self):
        self._status = ItemStatus.next(self.status)

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'
