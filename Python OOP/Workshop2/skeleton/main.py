from datetime import date, timedelta
from board import Board
from board_item import BoardItem
from event_log import EventLog
from task import Task

def add_days_to_now(d):
    return date.today() + timedelta(days=d)


task = Task('Test the application flow', 'Steven', add_days_to_now(2))
task.advance_status()
task.advance_status()
task.assignee = 'Not Steven'
print(task.history())