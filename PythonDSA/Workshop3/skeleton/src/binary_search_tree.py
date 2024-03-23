from src.bst_node import BSTNode

from collections import deque


class BinarySearchTree:
    def __init__(self, root=None):
        self._root: BSTNode = root

    @property
    def root(self):
        return self._root

    @property
    def height(self):
        def helper(node=self._root):
            if node is None:
                return 0
            return 1 + min(helper(node.left), helper(node.right))

        return helper()

    def dfs_inorder(self):
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.value)
            helper(node.right)

        res = []
        helper(self._root)
        return res

    def dfs_preorder(self):
        def helper(node):
            if not node:
                return
            res.append(node.value)
            helper(node.left)
            helper(node.right)

        res = []
        helper(self._root)
        return res

    def dfs_postorder(self):
        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.value)

        res = []
        helper(self._root)
        return res

    def bfs(self):
        if self._root is None:
            return
        res = []
        queue = deque()
        queue.append(self._root)
        while queue:
            node = queue.popleft()
            res.append(node.value)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def search(self, value):
        node = self._root
        while node is not None:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, value):
        new_node = BSTNode(value)
        if self._root is None:
            self._root = new_node
            return
        current = self._root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

    def remove(self, value):
        def find_min(node):
            while node.left is not None:
                node = node.left
            return node

        def delete_node(root, value):
            if root is None:
                return root
            if value < root.value:
                root.left = delete_node(root.left, value)
            elif value > root.value:
                root.right = delete_node(root.right, value)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                temp = find_min(root.right)
                root.value = temp.value
                root.right = delete_node(root.right, temp.value)
            return root

        self._root = delete_node(self._root, value)
