class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next: ListNode = next

    def __repr__(self):
        return f"Node {self.value}"

    def make_list(self):
        node = self
        the_list = []
        while node:
            the_list.append(node.value)
            node = node.next
        return the_list
