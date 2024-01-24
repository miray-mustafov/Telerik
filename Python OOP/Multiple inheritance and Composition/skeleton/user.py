from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from task import Task

from item_status import ItemStatus


class User:
    usernames = []

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self._assigned_tasks = []
        self._capacity = 3

    def __repr__(self):
        return f"User " + self.username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value or value in User.usernames:
            raise ValueError('This username is taken or invalid!')
        self._username = value
        User.usernames.append(self.username)

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Email must contain @")
        self._email = value

    @property
    def assigned_tasks(self):
        return tuple(self._assigned_tasks)

    @property
    def capacity(self):
        return self._capacity

    def user_has_that_task(self, task_title):
        if [x for x in self._assigned_tasks if x.title == task_title]:
            return True
        return False

    def receive_task(self, task):
        if not self.capacity:
            raise ValueError('Capacity full!')
        elif self.user_has_that_task(task.title):
            raise ValueError(f'Task with title {task.title} already assigned!')
        self._assigned_tasks.append(task)
        self._capacity -= 1

    def remove_task(self, task):
        if self.capacity == 3:
            raise ValueError('No tasks to remove!')
        elif not self.user_has_that_task(task.title):
            raise ValueError(f'Task {task.title} is not assigned to that user!')
        self._assigned_tasks.remove(task)
        self._capacity += 1

    def advance_task_status(self, task: "Task"):
        if self.username == task.assignee and task.status in [ItemStatus.TODO, ItemStatus.IN_PROGRESS]:
            raise ValueError('Task does not belong to that assignee!')
        elif task.status not in [ItemStatus.TODO, ItemStatus.IN_PROGRESS]:
            raise ValueError("Status can be advanced from TODO and IN PROGRES")
        task.advance_status()

    # def info(self):
    #     pass
