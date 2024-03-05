
from src.common.list_node import ListNode
from functools import reduce


def create_linked_list(*values):
    return reduce(lambda prev, curr: ListNode(curr, prev), reversed(values), None)


def compare_lists(a: ListNode, b: ListNode):
    while a and b:
        if a.value != b.value:
            return False

        a = a.next
        b = b.next

    return a is None and b is None


def serialize_list(head: ListNode):
    values = []
    while head:
        values.append(head.value)
        head = head.next

    return ','.join(values)
