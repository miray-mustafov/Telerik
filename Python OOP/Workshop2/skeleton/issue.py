from board_item import BoardItem
from item_status import ItemStatus

class Issue(BoardItem):
    def __init__(self, title, description, due_date):
        if not description:
            description = 'No description'
        self._description = description

        BoardItem._ensure_valid_title(title)
        BoardItem._ensure_valid_due_date(due_date)

        self._title = title
        self._due_date = due_date
        self._status = ItemStatus.OPEN

        self._history = []
        self._log_event(f'Issue created: {super().info()}')  # !!!

    @property
    def description(self):
        return self._description

    def info(self):
        board_item_info = super().info()
        return f"Issue ({self.description}) {board_item_info}"
