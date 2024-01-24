from datetime import date, timedelta
from board import Board
from issue import Issue
from task import Task


def add_days_to_now(d):
    return date.today() + timedelta(days=d)

