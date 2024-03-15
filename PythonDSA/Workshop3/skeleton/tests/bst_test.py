import unittest
from src.binary_search_tree import BinarySearchTree
from src.bst_node import BSTNode


def create_default_test_nodes():
    tree = BSTNode(5)
    tree.left = BSTNode(2)
    tree.right = BSTNode(8)
    tree.left.right = BSTNode(3)
    tree.right.left = BSTNode(6)
    tree.right.right = BSTNode(10)

    return tree


class BinarySearchTree_Test(unittest.TestCase):
    def test_height_returnsZero_emptyTree(self):
        # Arrange
        bst = BinarySearchTree()

        # Act & Assert
        self.assertEqual(0, bst.height)

    def test_height_returnsCorrectValue_notEmptyTree(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act & Assert
        self.assertEqual(2, bst.height)

    def test_search_returnsTrue_whenValueExists(self):
        # Arrange
        test_nodes = create_default_test_nodes()
        bst = BinarySearchTree()
        bst._root = test_nodes

        # Act & Assert
        self.assertTrue(bst.search(test_nodes.value))
        self.assertTrue(bst.search(test_nodes.left.value))
        self.assertTrue(bst.search(test_nodes.right.value))
        self.assertTrue(bst.search(test_nodes.left.right.value))
        self.assertTrue(bst.search(test_nodes.right.left.value))
        self.assertTrue(bst.search(test_nodes.right.right.value))

    def test_search_returnsFalse_whenValueDoesNotExist(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act & Assert
        self.assertFalse(bst.search(300))

    def test_insert_valuesAtCorrectPositions(self):
        # Arrange
        bst = BinarySearchTree()
        values = [5, 3, 7, 1, 4, 6, 9]

        # Act
        for value in values:
            bst.insert(value)

        # Assert
        root = bst.root
        self.assertEqual(5, root.value)
        # left subtree
        self.assertEqual(3, root.left.value)
        self.assertEqual(1, root.left.left.value)
        self.assertEqual(4, root.left.right.value)
        # right subtree
        self.assertEqual(7, root.right.value)
        self.assertEqual(6, root.right.left.value)
        self.assertEqual(9, root.right.right.value)

    def test_remove_removesLeafNode(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act
        bst.remove(6)

        # Asert
        self.assertIsNone(bst.root.right.left)

    def test_remove_removesNode_withOneChild(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act
        bst.remove(2)

        # Assert
        self.assertEqual(3, bst.root.left.value)
        self.assertIsNone(bst.root.left.right)

    def test_remove_removesNode_withTwoChildren(self):
        # this test assumes that this case is implemented by finding min_value in right tree
        # if you tried the other approach - max_value in left tree, the test will fail.
        # Sorry about that.

        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act
        bst.remove(5)

        # Assert
        self.assertEqual(6, bst.root.value)
        self.assertIsNone(bst.root.right.left)

    def test_remove_doesNothing_whenNoSuchValue(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act
        bst.remove(123)

        # Assert
        self.assertEqual(3, bst.root.left.right.value)
        self.assertEqual(6, bst.root.right.left.value)
        self.assertEqual(10, bst.root.right.right.value)

    def test_dfsinorder_returnsValues_inCorrectOrder(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act & Assert
        self.assertEqual([2, 3, 5, 6, 8, 10], bst.dfs_inorder())

    def test_dfspreorder_returnsValues_inCorrectOrder(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act & Assert
        self.assertEqual([5, 2, 3, 8, 6, 10], bst.dfs_preorder())

    def test_dfspostorder_returnsValues_inCorrectOrder(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act & Assert
        self.assertEqual([3, 2, 6, 10, 8, 5], bst.dfs_postorder())

    def test_bfs_returnsValues_inCorrectOrder(self):
        # Arrange
        bst = BinarySearchTree()
        bst._root = create_default_test_nodes()

        # Act & Assert
        self.assertEqual([5, 2, 8, 3, 6, 10], bst.bfs())
