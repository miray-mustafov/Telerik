from boards.board import Board
from boards.can_remove_item import CanRemoveItem
from boards.can_add_item import CanAddItem


class EditableBoard(Board, CanAddItem, CanRemoveItem):
    pass
