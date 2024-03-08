from src.linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode = None
        self._tail: LinkedListNode = None
        self._count = 0

    @property
    def count(self):
        return self._count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def _insert_before_head(self, value):
        new_head_node = LinkedListNode(value)
        if not self._count:
            self._head = self._tail = new_head_node
            return

        new_head_node.next = self._head
        self._head.prev = new_head_node
        self._head = new_head_node

    def _insert_after_tail(self, value):
        new_tail_node = LinkedListNode(value)
        if not self._count:
            self._head = self._tail = new_tail_node
            return

        new_tail_node.prev = self._tail
        self._tail.next = new_tail_node
        self._tail = new_tail_node

    def add_first(self, value):
        self._insert_before_head(value)
        self._count += 1

    def add_last(self, value):
        self._insert_after_tail(value)
        self._count += 1

    def insert_after(self, node, value):
        if not self._count:
            raise ValueError('LinkedList empty!')

        if self._tail == node:
            self._insert_after_tail(value)
        else:
            new_node = LinkedListNode(value)
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node

        self._count += 1

    def insert_before(self, node, value):
        if not self._count:
            raise ValueError('LinkedList empty!')

        if self._head == node:
            self._insert_before_head(value)
        else:
            new_node = LinkedListNode(value)
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node

        self._count += 1

    def remove_first(self):
        if not self._count:
            raise ValueError('LinkedList empty!')

        head_to_remove = self._head
        if self._count == 1:
            self._head = self._tail = None
        else:
            head_to_remove.next.prev = None
            self._head = head_to_remove.next

        self._count -= 1
        return head_to_remove.value

    def remove_last(self):
        if not self._count:
            raise ValueError('LinkedList empty!')

        tail_to_remove = self._tail
        if self._count == 1:
            self._head = self._tail = None
        else:
            tail_to_remove.prev.next = None
            self._tail = tail_to_remove.prev

        self._count -= 1
        return tail_to_remove.value

    def find(self, value):
        cur_node = self._head
        while cur_node:
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.next

        return None

    def values(self):
        listt = []
        cur_node = self._head
        while cur_node:
            listt.append(cur_node.value)
            cur_node = cur_node.next

        return tuple(listt)
