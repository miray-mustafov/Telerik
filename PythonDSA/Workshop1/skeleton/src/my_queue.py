from src.linked_list_node import LinkedListNode


class CustomQueue:
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

    def enqueue(self, val):
        node = LinkedListNode(val)
        if self.is_empty:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self._count += 1

    def dequeue(self):
        if self.is_empty:
            raise ValueError('Queue is empty!')
        head_to_remove = self.head
        self.head = self.head.next

        if self._count == 1:  # todo
            self.tail = None

        self._count -= 1
        return head_to_remove.value

    def peek(self):
        if self.is_empty:
            raise ValueError('Queue is empty!')
        return self.head.value


q = CustomQueue()
print(q.is_empty)
print(q.enqueue(1))
print(q.is_empty)
print()
print(q.enqueue(2))
print(q.dequeue())
print(q.dequeue())
print(q.is_empty)
