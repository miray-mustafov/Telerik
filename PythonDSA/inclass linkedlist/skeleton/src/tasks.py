from src.common.list_node import ListNode
from src.common.stack import Stack

LIST123 = [1, 2, 3]
LIST1234 = [1, 2, 3, 4]


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


h1 = generate_LL_from_list(LIST123)
h2 = generate_LL_from_list(LIST1234)
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
res_h1: ListNode = merge_sorted_lists(h1, h2)
print(res_h1.make_list())


# task 3
# [1, 2, 3, 4]
def reverse_list(head: ListNode):
    if not head or not head.next:
        return head

    prev_node = None
    cur_node = head

    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node

        prev_node = cur_node
        cur_node = next_node

    return prev_node


h1 = generate_LL_from_list(LIST1234)
reversed_h1 = reverse_list(h1)
print(reversed_h1.make_list())


# task 4

def validate_parentheses(expr: str):
    my_stack = []
    for el in expr:
        if el == '(':
            my_stack.append(el)
        elif el == ')':
            if not my_stack:
                return False
            my_stack.pop()

    if my_stack:
        return False
    return True


expression1 = "1 + (2 * 3)"
expression2 = "2 + (1 + (2 * 3)"
print(validate_parentheses(expression1))
print(validate_parentheses(expression2))


# task 5


def backspace_char(sequence: str):
    my_stack = []
    for el in sequence:
        if my_stack and el == '#':
            my_stack.pop()
        elif el != '#':
            my_stack.append(el)
    return ''.join(my_stack)


seq1 = 'abc#d'  # 'abd'
seq2 = 'abcd##e##'  # 'a'
print(backspace_char(seq1))
print(backspace_char(seq2))
print(backspace_char("abc####de"))  # 'de'
