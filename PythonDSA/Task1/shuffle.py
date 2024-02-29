"""
Shuffle
Your task is to implement a brand new algorithm for shuffling numbers. The numbers will be from 1 to N. You will receive K numbers, which will be the ones you will shuffle following the rules below:

If the number to be shuffled is even -> move it after the number with value = numberToBeShuffled / 2 (i.e. if you need to shuffle 4 you need to move it after 2).
If the number to be shuffled is odd -> move it after the number with value = numberToBeShuffled * 2 (i.e. if you need to shuffle 3 you need to move it after 6). If numberToBeShuffled * 2 > N move it after the number with value N.
If the number to be shuffled should be moved after the same number -> do nothing.
Input
Read from the standard input
On the first line, find the number N and K
N - numbers will be from 1 to N
K - the count of numbers which will be found on the next line of the input
On the next line there will be K numbers
The numbers to be shuffled (all in range from 1 to N)
Output
Print on the standard output
On a single line, print the shuffled numbers
Constraints
1 <= N <= 100
1 <= K <= 400 000
Sample tests
Input
7 4
1 5 4 7
Output
2 4 1 3 6 7 5
Explanation
You have the numbers 1 2 3 4 5 6 7. First you need to move 1 which is odd, so we move it after 1 * 2 = 2 -> 2 1 3 4 5 6 7
Move 5 which is odd, so we should move it after 5 * 2 = 10, but it is greater than 7, so we move it after 7 -> 2 1 3 4 6 7 5
Move 4 which is even, so we move it after 4 / 2 = 2 -> 2 4 1 3 6 7 5
Move 7 which is odd, so we should move it after 7 * 2 = 14, but it is greater than 7, so we need to move it after 7, which is the number to be moved, so we do nothing -> 2 4 1 3 6 7 5
Input
10 5
10 2 1 6 8
Output
2 1 3 6 4 8 5 10 7 9
Input
5 5
1 2 1 2 5
Output
1 2 3 4 5
"""


class LinkedListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev: LinkedListNode = prev
        self.next: LinkedListNode = next

    def __repr__(self):
        return f'n{self.value}'


class DoublyLinkedList:
    def __init__(self):
        self.head: LinkedListNode = None
        self.d = {}  # build d{person_name: node}
        self.n = None

    def move_n1_after_n2(self, n1_val, n2_val):
        if n2_val > self.n:
            n2_val = self.n
        if n1_val == n2_val:
            return

        n1, n2 = self.d[n1_val], self.d[n2_val]
        if n2.next == n1:  # case when n1 is already after n2
            return

        # following paragraph ! when n2 and n1 are at the edges
        dummy_head = None
        dummy_tail = None
        if n1 == self.head:
            dummy_head = LinkedListNode(0, next=self.head)
            self.head.prev = dummy_head
        elif n1.next is None:
            dummy_tail = LinkedListNode(0, prev=n1)
            n1.next = dummy_tail
        if n2.next is None:
            dummy_tail = LinkedListNode(0, prev=n2)
            n2.next = dummy_tail

        # the actual swap
        n1.prev.next = n1.next
        n1.next.prev = n1.prev
        n2.next.prev = n1
        n1.next = n2.next
        n2.next = n1
        n1.prev = n2

        if dummy_head:
            self.head = dummy_head.next
        if dummy_tail:
            dummy_tail.prev.next = None
        a = 5

    def initialize_dll_from_n(self, n: int):
        self.head = LinkedListNode(1)
        self.d[1] = self.head
        self.n = n

        node = self.head
        for i in range(2, n + 1):
            node.next = LinkedListNode(i, prev=node)

            node = node.next
            self.d[i] = node

    def print_to_console(self):
        node = self.head
        output = []
        while node:
            output.append(str(node.value))
            node = node.next
        print(' '.join(output))


n, swaps = map(int, input().split())
nums_for_swap = [int(n) for n in input().split()]
dll = DoublyLinkedList()
dll.initialize_dll_from_n(n)
for num in nums_for_swap:
    num2 = (num * 2) if num % 2 == 1 else (num // 2)
    dll.move_n1_after_n2(num, num2)
dll.print_to_console()
