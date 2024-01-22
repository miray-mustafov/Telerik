from board_item import BoardItem
from item_status import ItemStatus


class Task(BoardItem):
    def __init__(self, title, assignee, due_date):
        super().__init__(title, due_date)
        Task._ensure_valid_assignee(assignee)

        self._assignee = assignee
        self._status = ItemStatus.TODO
        self._history = []
        self._log_event(f'Item created: {self.info()}')

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        Task._ensure_valid_assignee(value)
        self._log_event(f"Assignee changed from {self.assignee} to {value}")
        self._assignee = value

    @staticmethod
    def _ensure_valid_assignee(assignee):
        if not 5 <= len(assignee) <= 30:
            raise ValueError("Assignee len between 5 and 30")
