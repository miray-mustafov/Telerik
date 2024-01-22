from board_item import BoardItem


class Issue(BoardItem):
    def __init__(self, title, description, due_date):
        super(Issue, self).__init__(title, due_date)
        if not description:
            description = 'No description'
        self._description = description

    @property
    def description(self):
        return self._description