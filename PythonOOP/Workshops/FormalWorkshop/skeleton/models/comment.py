from core import validate


class Comment:
    CONTENT_LEN_MIN = 3
    CONTENT_LEN_MAX = 200
    CONTENT_LEN_ERR = f'Content must be between {CONTENT_LEN_MIN} and {CONTENT_LEN_MAX} characters long!'

    def __init__(self, content, author):
        self.content: str = content
        self.author: str = author

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        value = validate.str_len(value, Comment.CONTENT_LEN_MIN, Comment.CONTENT_LEN_MAX, Comment.CONTENT_LEN_ERR)
        self._content = value

    @property
    def author(self):
        return self._author

    @author.setter  # my
    def author(self, value):
        value = validate.str_len(value, 2, 20, 'Author must be between 2 and 20 characters long!')
        self._author = value

    def __str__(self):
        res = '\n'.join([
            '----------',
            self.content,
            f'User: {self.author}',
            '----------', ])
        return res
