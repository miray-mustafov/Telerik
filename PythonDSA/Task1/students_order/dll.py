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

    @property
    def count(self):
        return len(self.d)

    def move_p1_tothe_left_of_p2(self, p1_name, p2_name):
        p1, p2 = self.d[p1_name], self.d[p2_name]
        if p1.next == p2:  # case when p1 is already left seated to p2
            return

        # following paragraph ! when p2 and p1 are at the edges
        dummy_head = None
        dummy_tail = None
        if p2 == self.head or p1 == self.head:
            dummy_head = LinkedListNode(0, next=self.head)
            self.head.prev = dummy_head
        if p1.next == None:
            dummy_tail = LinkedListNode(0, prev=p1)
            p1.next = dummy_tail
        elif p2.next == None:  # case 8
            dummy_tail = LinkedListNode(0, prev=p2)
            p2.next = dummy_tail

        # the actual swap
        p1.prev.next = p1.next
        p1.next.prev = p1.prev
        p2.prev.next = p1
        temp_p2_prev = p2.prev
        p2.prev = p1
        p1.prev = temp_p2_prev
        p1.next = p2

        if dummy_head:
            self.head = dummy_head.next
        if dummy_tail:
            dummy_tail.prev.next = None
        a = 5

    def initialize_dll_from_list(self, l: list):
        if len(l) < 2:
            raise ValueError("Elements in the list are < 2!")

        first_value = l[0]
        self.head = LinkedListNode(first_value)
        self.d[first_value] = self.head

        node, i = self.head, 1
        for el in l[1:]:
            node.next = LinkedListNode(el, prev=node)

            node, i = node.next, i + 1
            self.d[el] = node
        # todo ? self.tail = node

    def print_to_console(self):
        node = self.head
        output = []
        while node:
            output.append(node.value)
            node = node.next
        print(' '.join(output))
