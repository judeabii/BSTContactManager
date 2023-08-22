# BSTContactManager
BSTContactManager is a contact management system implemented using a Binary Search Tree (BST) data structure. This repository provides an efficient and organized solution for storing, retrieving, and managing contact information.

Leveraging the benefits of a self-balancing BST (AVL tree), the system ensures fast and accurate search operations, maintaining contacts in sorted order for easy browsing.

Key Features:
- Efficient searching and retrieval of contacts using a Binary Search Tree.
- Sorted order maintenance for quick browsing and management.
- Insertion, Updating and Deleting of contacts while preserving balanced tree structure.
- Flexible duplicate handling options.
- Traversal methods for comprehensive contact list exploration.

### AVL tree implementation
```commandline
    if height(node.left) - height(node.right) < -1:                 # Right Heavy Tree
        if height(node.right.right) >= height(node.right.left):     # LL rotation
            node = left_rotation(node)
        else:                                                       # RL rotation
            node.right = right_rotation(node.right)
            node = left_rotation(node)
    if height(node.left) - height(node.right) > 1:                  # Left Heavy Tree
        if height(node.left.left) >= height(node.left.right):       # RR rotation
            node = right_rotation(node)
        else:                                                       # LR rotation
            node.left = left_rotation(node.left)
            node = right_rotation(node)
```
#### Code for left rotation
```commandline
def left_rotation(root): 
    new_root = root.right
    root.right = new_root.left
    new_root.left = root

    return new_root
```
#### Code for right rotation
```commandline
def right_rotation(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root

    return new_root
```