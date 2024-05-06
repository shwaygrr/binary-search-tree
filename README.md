# Binary Search Tree (BST) Library
This is a simple Python library for working with Binary Search Trees (BSTs). It provides functionality to build a BST from an array, insert nodes, delete nodes, search for nodes, find the minimum and maximum nodes in a subtree, and find the successors and predecessors of nodes.

## Installation
You can simply copy the `bst.py` file into your project directory and import it as needed.

## Usage
```python
from bst import BinarySearchTree

# Example usage
bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])

bst.printTree()  # Print the BST

bst.search(4)  # Search for a node with value 4

bst.insert(9)  # Insert a node with value 9

bst.delete(6)  # Delete the node with value 6

bst.treeMin()  # Find the minimum value node in the BST

bst.successor(5)  # Find the successor of the node with value 5

# and more...
```

## Documentation
### `class TreeNode`
Represents a node in a Binary Search Tree (BST).

#### Attributes:
- `value`: The value stored in the node.
- `left`: Reference to the left child node.
- `right`: Reference to the right child node.

#### Methods:
- `__init__(self, value=None)`: Initializes a TreeNode with the given value.

### `class BinarySearchTree`
Represents a Binary Search Tree (BST).

#### Attributes:
- `root`: The root node of the BST.

#### Methods:
- `__init__(self, arr=None)`: Initializes a BinarySearchTree with an optional array to build the tree.
- `buildTree(self, arr)`: Builds a BST from the given array.
- `printTree(self)`: Prints the BST in a tree-like format. [Credit](https://stackoverflow.com/a/72497198/23355472)
- `search(self, value)`: Searches for a node with the given value in the BST.
- `parent(self, value)`: Finds the parent of a node with the given value in the BST.
- `insert(self, value)`: Inserts a node with the given value into the BST.
- `treeMin(self, subtree_key=None)`: Finds the minimum value node in the subtree rooted at the given key.
- `treeMax(self, subtree_key=None)`: Finds the maximum value node in the subtree rooted at the given key.
- `successor(self, node_key)`: Finds the successor of a node with the given key in the BST.
- `predecessor(self, node_key)`: Finds the predecessor of a node with the given key in the BST.
- `delete(self, value)`: Deletes the node with the given value from the BST.

## References
Algorithms and some of the implementation details were adapted from the book:

Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. (2009). *Introduction to Algorithms*, 3rd edition. The MIT Press. ISBN: 0262033844.

## License
This library is licensed under the MIT License
