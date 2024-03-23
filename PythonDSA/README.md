<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

# Trees - In class activity

A binary search tree (BST), is a node-based data structure in which each node has **no more than two child nodes.** Each child must either be a leaf node or the root of another binary search tree. The left sub-tree contains only nodes with values less than the parent node; the right sub-tree contains only nodes with values greater than the parent node. 

## Binary search tree characteristics:

- The root is a special node with no parents;
- A leaf is a node with no child nodes;
- A tree is balanced when for each node X the difference in height of the left and the right sub-trees is <= 1
- Balanced tree is optimized for searching, inserting and deleting which are done in `O(logn)` complexity;

### Common operations and their time complexities (in a balanced tree):

- Insert new node: `O(logn)`
- Search: `O(logn)`
- Remove a node: `O(logn)`
- In a non-balanced BST, the performance of some operations may degrade to `O(n)`.

## Binary search tree example:

![picture](images/bst.png)

## Binary search tree practical use-cases:

- Have a sorted list of values where you can quickly add elements and still have them sorted (Consider using an array for this purpose. You have very fast access to read random values, but if you want to add a new value, you have to find the place in the array where it belongs, shift everything over, and then insert the new value);
- Maintaining a dynamically changing dataset in sorted order, for some "sortable / comparable" type;

### Before you begin:

- Get a better understanding of trees by playing around in [Visualgo](https://visualgo.net/en/bst);
- Draw a BST. Think about the algorithms to insert and find a node. What about deleting? How would you implement removing a node;

## Task

Your task is to implement a binary search tree, using the skeleton provided. The unit tests cover the following methods and properties:

- `insert(value) -> None` - inserts the given value in the tree. Does nothing if the value already exists
- `search(value) -> boolean` - returns whether the given value exists in the tree
- `height -> int` - returns the height of the tree
- `dfs_inorder -> list` - returns a list of all values in *inorder* fashion. If done correctly, the array should be **naturally sorted**.
- `bfs` - returns an array of all values in breadth-first search order.
- `dfs_preorder() -> list` - returns a list of all values in *preorder* fashion.
- `dfs_postorder() -> list` - returns a list of all values in *postorder* fashion.

The `_root` attribute and `root` property are part of the skeleton and are used for easier testing. **Do not delete them**.

### Advanced task

- Implement `remove(value) -> None` - removes the given value from the tree.

<details>
  <summary>Very Advanced Task</summary>

  <p>
  <i>This task is complicated, you can try it after you have graduated and you need some practice between interviews.</i>

  - Refactor the tree to be a **balanced** Binary Search Tree. You approach the problem by learning about AVL trees or Red-Black Trees (or both).
  </p>
</details>


