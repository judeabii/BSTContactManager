class Contacts:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.right = None
        self.left = None
        self.height = None

    def __str__(self):
        return f"{self.name} - {self.number}"


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

    node.height = height(node)
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
    return node


def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)

    return 1 + max(left, right)


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


def find(node, name):
    found_contact = None
    if node is None:
        return node
    if node.name == name:
        found_contact = node
        return found_contact
    elif node.name > name:
        found_contact = find(node.right, name)
    elif node.name < name:
        found_contact = find(node.left, name)

    return found_contact


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node)
        inorder(node.right)


def preorder(node):
    if node is not None:
        print(node)
        preorder(node.left)
        preorder(node.right)


def right_rotation(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root

    return new_root


def left_rotation(root):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root

    return new_root


if __name__ == "__main__":
    root = None
    root = insert(root, "Mounika", 99880000)
    root = insert(root, "Jude", 95910000)
    root = insert(root, "Brownie", 7258200)

    while True:
        input_option = input("Create New Contact \t\t--> [1]\nUpdate Existing Contact --> [2]\n"
                             "Find Contact \t\t\t--> [3]\nShow All Contacts \t\t--> [4]\n")

        if input_option not in ("1", "2", "3", "4"):
            print("You have entered a wrong option, try again.\n")
            continue

        if input_option == "1":
            name = input("Enter the Name\n")
            number = input("Enter the Number\n")
            root = insert(root, name, number)

        if input_option == "2":
            name = input("Enter the Name\n")
            number = input("Enter updated contact number\n")
            contact = update(root, name, number)
            if contact is None:
                print(f"No contact with name: {name} exists.")
            else:
                print(f"Contact: {contact.name} has been updated with the number: {contact.number}")

        if input_option == "3":
            name = input("Enter the Name\n")
            contact = find(root, name)
            if contact is None:
                print(f"No contact with name: {name} exists.")
            else:
                print(contact)

        if input_option == "4":
            if root is None:
                print("Contact list is empty")
            else:
                preorder(root)

        go_again = input("Show Menu Again? (Y)\n")
        if go_again in ("Y", "y"):
            continue
        else:
            print("Thank you!")
            break
