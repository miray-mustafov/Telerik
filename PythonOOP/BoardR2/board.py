from board_item import BoardItem


class Board:
    def __init__(self):
        self._items = []

    @property
    def count(self):
        return len(self._items)

    def add_item(self, item: BoardItem):
        # for el in self._items:
        #     if item.title == el.title:
        #         return
        if item in self._items:
            raise ValueError("Item already in the list")
        self._items.append(item)
