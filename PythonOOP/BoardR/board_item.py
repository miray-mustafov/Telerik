from item_status import ItemStatus
from datetime import date, timedelta


def add_days_to_now(d):
    if d < 0:
        raise ValueError("days must be positive")
    return date.today() + timedelta(days=d)


class BoardItem:
    def __init__(self, title, due_date):
        if not isinstance(title, str) or not 5 <= len(title) <= 30:
            raise ValueError("wrong title!")
        self.title = title
        self.due_date = due_date
        self.status = ItemStatus.OPEN

    def advance_status(self):
        self.status = ItemStatus.next(self.status)
        return self.status

    def revert_status(self):
        self.status = ItemStatus.previous(self.status)
        return self.status

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'
