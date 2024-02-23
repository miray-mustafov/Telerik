from typing import TYPE_CHECKING
from abc import abstractmethod

if TYPE_CHECKING:
    from board_items.board_item import BoardItem


class CanAddItem:
    @abstractmethod
    def add_item(self, item: "BoardItem"):
        if item in self._items:
            raise ValueError('BoardItem already in the list')
        self._items.append(item)
