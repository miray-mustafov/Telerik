from board_items.board_item import BoardItem
from users.user import User
from board_items.task import Task
from board_items.item_status import ItemStatus


class Board():
    def __init__(self):
        self._items = []
        self._users = []

    @property
    def team_capacity(self):
        return sum([x.capacity for x in self._users])

    @property
    def users(self):
        return tuple(self._users)

    @property
    def count(self):
        return len(self._items)

    def add_item(self, item: BoardItem):
        if item in self._items:
            raise ValueError('BoardItem already in the list')

        self._items.append(item)

    def add_user(self, username, email):
        # if [user.username for user in self._users if user.username == username]:
        #     raise ValueError('This username already exists!')
        new_user = User(username, email)
        self._users.append(new_user)
        return new_user

    @staticmethod
    def reassign_task(task: Task, new_assignee: User):
        old_assignee = task.assignee
        if old_assignee == new_assignee:
            raise ValueError('Cannot reassign_task to same assignee!')
        old_assignee.remove_task(task)
        task._status = ItemStatus.TODO
        task.assignee = new_assignee
        new_assignee.receive_task(task)
