from src.linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode = None
        self._tail: LinkedListNode = None
        self._count = 0

    @property
    def count(self):
        raise NotImplementedError()

    @property
    def head(self):
        raise NotImplementedError()

    @property
    def tail(self):
        raise NotImplementedError()

    def add_first(self, value):
        raise NotImplementedError()

    def add_last(self, value):
        raise NotImplementedError()

    def insert_after(self, node, value):
        raise NotImplementedError()

    def insert_before(self, node, value):
        raise NotImplementedError()

    def remove_first(self):
        raise NotImplementedError()

    def remove_last(self):
        raise NotImplementedError()

    def find(self, value):
        raise NotImplementedError()

    def values(self):
        raise NotImplementedError()

    def _insert_before_head(self, value):
        raise NotImplementedError()

    def _insert_after_tail(self, value):
        raise NotImplementedError()
