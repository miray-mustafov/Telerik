from src.linked_list_node import LinkedListNode


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
        node = LinkedListNode(val)
        if self.is_empty:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self._count += 1

    def pop(self):
        if self.is_empty:
            raise ValueError('Stack is empty!')
        tail_to_remove = self.head
        self.tail = self.tail.next
        self._count -= 1
        return tail_to_remove.value

    def peek(self):
        if self.is_empty:
            raise ValueError('Stack is empty!')
        return self.tail.value

