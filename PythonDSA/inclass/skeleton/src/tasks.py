from src.common.list_node import ListNode
from src.common.stack import Stack

LIST1 = [1, 2, 3]
LIST2 = [1, 2, 3, 4]


def generate_LL_from_list(nums):
    node = ListNode(nums[-1])
    for i in range(len(nums) - 2, -1, -1):
        node = ListNode(nums[i], node)
    return node


# task 1

def find_middle_of_list(head: ListNode):
    if not head:
        return None

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


h1 = generate_LL_from_list(LIST1)
h2 = generate_LL_from_list(LIST2)
print(find_middle_of_list(h1))  # node 2
print(find_middle_of_list(h2))  # node 3


# task 2

def merge_sorted_lists(h1: ListNode, h2: ListNode):
    dummy = ListNode(0)
    node = dummy
    while h1 and h2:
        if h1.value <= h2.value:
            node.next = h1
            h1 = h1.next
        else:
            node.next = h2
            h2 = h2.next
        node = node.next

    if h1:
        node.next = h1
    elif h2:
        node.next = h2

    return dummy.next


h1 = generate_LL_from_list([1, 2, 3])
h2 = generate_LL_from_list([1, 4])
res_h: ListNode = merge_sorted_lists(h1, h2)
print(res_h.make_list())


# task 3

def reverse_list(head: ListNode):
    raise NotImplementedError()


# task 4

def validate_parentheses(expr: str):
    raise NotImplementedError()


# task 5

def backspace_char(sequence: str):
    raise NotImplementedError()
