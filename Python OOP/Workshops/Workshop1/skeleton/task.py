from board_item import BoardItem
from item_status import ItemStatus


class Task(BoardItem):
    def __init__(self, title, assignee, due_date):
        Task._ensure_valid_assignee(assignee)
        self._assignee = assignee

        BoardItem._ensure_valid_title(title)
        BoardItem._ensure_valid_due_date(due_date)
        self._title = title
        self._due_date = due_date
        self._status = ItemStatus.TODO

        self._history = []
        self._log_event(f'Task created: {super().info()}')  # !!!

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        Task._ensure_valid_assignee(value)
        self._log_event(f"Assignee changed from {self.assignee} to {value}")
        self._assignee = value

    def info(self):
        board_item_info = super().info()
        return f"Task (assigned to: {self.assignee}) {board_item_info}"

    @staticmethod
    def _ensure_valid_assignee(assignee):
        if not 5 <= len(assignee) <= 30:
            raise ValueError("Assignee len between 5 and 30")
