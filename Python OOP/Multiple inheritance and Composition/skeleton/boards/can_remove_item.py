from typing import TYPE_CHECKING
from abc import abstractmethod

if TYPE_CHECKING:
    from board_items.board_item import BoardItem


class CanRemoveItem:
    @abstractmethod
    def remove_item(self, item: "BoardItem"):
        self._items.remove(item)
