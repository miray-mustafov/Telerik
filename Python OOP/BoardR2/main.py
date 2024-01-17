from datetime import date, timedelta
from board import Board
from board_item import BoardItem
from event_log import EventLog


def add_days_to_now(d):
    return date.today() + timedelta(days=d)
