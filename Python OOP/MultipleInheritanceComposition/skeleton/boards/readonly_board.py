from boards.board import Board
from boards.can_add_item import CanAddItem


class ReadonlyBoard(Board, CanAddItem):
    pass
