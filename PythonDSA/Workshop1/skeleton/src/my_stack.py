from src.linked_list_for_stack import LinkedListNodeStack


class CustomStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    @property
    def count(self):
        return self._count

    @property
    def is_empty(self):
        if self.head:
            return False
        return True

    def push(self, val):
        node = LinkedListNodeStack(val)
        if self.is_empty:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self._count += 1

    def pop(self):
        if self.is_empty:
            raise ValueError('Stack is empty!')

        tail_to_remove = self.tail
        if self._count == 1:
            self.head = self.tail = None
        else:
            tail_to_remove.prev.next = None
            self.tail = tail_to_remove.prev

        self._count -= 1
        return tail_to_remove.value

    def peek(self):
        if self.is_empty:
            raise ValueError('Stack is empty!')
        return self.tail.value
