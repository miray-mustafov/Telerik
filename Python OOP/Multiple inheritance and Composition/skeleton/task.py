from board_item import BoardItem
from datetime import date
from item_status import ItemStatus
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User


class Task(BoardItem):
    def __init__(self, title: str, assignee: "User", due_date: date):
        self._assignee = assignee
        super().__init__(title, due_date, ItemStatus.TODO)

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        self._log_event(f'Assignee changed from {self._assignee.username} to {value.username}')
        self._assignee = value

    def info(self):
        return f'Task (assigned to: {self.assignee.username}) {super().info()}'

    def __repr__(self):
        return f'Task {self.title} user:{self.assignee}'
