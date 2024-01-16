from datetime import date, timedelta
from board import Board
from board_item import BoardItem
from event_log import EventLog


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


item = BoardItem('Refactor this mess', add_days_to_now(2))
anotherItem = BoardItem('Dont refactor anything',  add_days_to_now(2))

board = Board()
board.add_item(item)
board.add_item(anotherItem)
board.add_item(item) # nothing happens
board.add_item(item) # nothing happens

print(board.count) # 2