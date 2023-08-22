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

### Insertion
```commandline
def insert(node, name, number):
    if node is None:
        node = Contacts(name, number)
        node.height = 1
        return node
    if node.name > name:
        node.left = insert(node.left, name, number)
    elif node.name < name:
        node.right = insert(node.right, name, number)
    elif node.name == name:
        print(f"This contact name already exists : {node.name}")
        return node
        
    # AVL implementation
    
    return node
```
The above code is followed by the AVL implementation code to make sure that the BST remains balanced after insertion.

### Deletion
```commandline
def delete(node, name):
    if node is None:
        return None
    if node.name == name:
        if node.right is None and node.left is None:
            deleted_contact[0] = node
            return None
        if node.right is None and node.left:
            deleted_contact[0] = node
            return node.left
        if node.left is None and node.right:
            deleted_contact[0] = node
            return node.right
        if node.left and node.right:
            deleted_contact[0] = node
            node.name = traverse_left(node.right)
            node.right = delete(node.right, node.name)
    elif node.name < name:
        node.right = delete(node.right, name)
    elif name < node.name:
        node.left = delete(node.left, name)
        
    # AVL implementation
    
    return node
```
The above code is followed by the AVL implementation code to make sure that the BST remains balanced after deletion.

### Update
```commandline
def update(node, name, number):
    search_value = None
    if node is None:
        return node
    if node.name == name:
        node.number = number
        return node
    elif node.name > name:
        search_value = update(node.right, name, number)
    elif node.name < name:
        search_value = update(node.left, name, number)

    return search_value
```

### Search/Find
```commandline
def find(node, name):
    found_contact = None
    if node is None:
        return node
    if node.name == name:
        found_contact = node
        return found_contact
    elif node.name > name:
        found_contact = find(node.left, name)
    elif node.name < name:
        found_contact = find(node.right, name)

    return found_contact
```