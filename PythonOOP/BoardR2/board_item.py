from datetime import date
from item_status import ItemStatus
from event_log import EventLog


class BoardItem:
    @staticmethod
    def validate_title(title):
        if len(title) < 5 or len(title) > 30:
            raise ValueError('Illegal title length [5:30]')
        return True

    @staticmethod
    def validate_due_date(due_date):
        if (due_date < date.today()):
            raise ValueError('Due date cant be in the past.')
        return True

    def __init__(self, title: str, due_date: date):
        BoardItem.validate_title(title)
        self._title = title
        BoardItem.validate_due_date(due_date)
        self._due_date = due_date
        self._status = ItemStatus.OPEN
        self._event_logs = [EventLog(f'Item created: {self.info()}')]

    @property
    def status(self):
        return self._status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        BoardItem.validate_title(value)
        self._event_logs.append(EventLog(f"Title changed from {self.title} to {value}"))
        self._title = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        BoardItem.validate_due_date(value)
        self._event_logs.append(EventLog(f"DueDate changed from {self.due_date} to {value}"))
        self._due_date = value

    def revert_status(self):
        if self.status == ItemStatus.OPEN:
            ev_log = EventLog(f'Cant change status, already at {self.status}')
        else:
            ev_log = EventLog(f'Status changed from {self.status} to {ItemStatus.previous(self.status)}')
        self._event_logs.append(ev_log)
        self._status = ItemStatus.previous(self.status)

    def advance_status(self):
        if self.status == ItemStatus.VERIFIED:
            ev_log = EventLog(f'Cant change status, already at {self.status}')
        else:
            ev_log = EventLog(f'Status changed from {self.status} to {ItemStatus.next(self.status)}')
        self._event_logs.append(ev_log)
        self._status = ItemStatus.next(self.status)

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'

    def history(self):
        res = ''
        for x in self._event_logs:
            res += f'{x.info()}\n'
        return res[:-1]
