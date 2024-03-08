from src.common.list_node import ListNode


# class ListNode:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next: ListNode = next

class Stack:
    def __init__(self):
        self._top: ListNode = None

    def push(self, value):
        self._top = ListNode(value, self._top)

    def pop(self):
        val = self._top.value
        self._top = self._top.next

        return val

    def peek(self):
        return self._top.value

    def is_empty(self):
        return self._top is None
