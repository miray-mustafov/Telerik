from datetime import date, timedelta
from board import Board
from issue import Issue
from task import Task
from user import User


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


board = Board()
steven = board.add_user("Steven", "steven@asd.bg")
task1 = Task('Test the application flow', steven, add_days_to_now(2))
steven.receive_task(task1)
board.add_item(task1)
print(f"Capacity of the team: {board.team_capacity}")
peter = board.add_user("Peter", "peter@asd.bg")
print(f"Capacity of the team: {board.team_capacity}")
print("============================================")
task2 = Task('Fix authentication', steven, add_days_to_now(2))
board.add_item(task2)
peter.receive_task(task2)
print(f"Capacity of the team: {board.team_capacity}")
print(task1.status)
steven.advance_task_status(task1)
print(task1.status)
board.reassign_task(task1, peter)
print(f"Steven assigned tasks: {steven.assigned_tasks}")
print(f"Peter assigned tasks: {[task.info() for task in peter.assigned_tasks]}")
print(task1.status)
peter.advance_task_status(task1)
print(task1.status)
peter.advance_task_status(task1)
print(task1.status)
print(f"Capacity of the team: {board.team_capacity}")
print(task1.history())