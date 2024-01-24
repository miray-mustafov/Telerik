from datetime import date
from board_items.board_item import BoardItem
from board_items.item_status import ItemStatus


class Issue(BoardItem):
    def __init__(self, title: str, description: str, due_date: date):
        self._description = description if description else 'No description'
        super().__init__(title, due_date, ItemStatus.OPEN)

    @property
    def description(self):
        return self._description

    def info(self):
        return f'Issue ({self.description}) {super().info()}'
