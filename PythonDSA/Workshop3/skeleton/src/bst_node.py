class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: BSTNode = left
        self.right: BSTNode = right

    def __repr__(self):
        return f"n{self.value}"
