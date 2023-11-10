class Node:
    def __init__(self, data = None):
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.data = data

def print_tree(node):
    if node:
       print_tree(node.left_child)
       print(node.data)
       print_tree(node.right_child)
    return

def insert(node, value):
    if node.data is None:
        node.data = value
        return
    if value < node.data:
        if node.left_child is None:
            node.left_child = Node(value)
            node.left_child.parent = node
            return
        insert(node.left_child, value)
    if value > node.data:
        if node.right_child is None:
            node.right_child = Node(value)
            node.right_child.parent = node
            return
        insert(node.right_child, value)


def search(node, value):
        if (node is None) or (node.data == value):
            return node
        if node.data < value:
            return search(node.right_child, value)
        return search(node.left_child, value)

def delete(root, value):
    if root == None:
        return root
    if root.data > value:
        root.left_child = delete(root.left_child, value)
        return root
    if root.data < value:
        root.right_child = delete(root.right_child, value)
        return root

    # We have a node which we want to delete and we'll be checking with case we have.
    # 1. We need to delete the leaf node.
    if root.left_child == None and root.left_child == None:
        del root
        return None

    # 2.a We need to delete the node which has only the right child.
    if root.left_child == None:
        new_root = root.right_child
        del root
        return new_root

    # 2.b We need to delete the node which has only the left child
    if root.right_child == None:
        new_root = root.left_child
        del root
        return new_root

    # 3. We need to delete the node which has two children.


def get_inorder_successor(node: Node):
    """
    We need to find and return the node with the smallest value, but greater that the value of our input node.
    So in other words, we need to get the next node after our given node in the ascending order.
    When our node has a right tree we need to find the leftmost node. And when we don't have the right tree we need to go up until we find a node with a value greater than our.
    """
    right_tree = node.right_child
    if right_tree is not None:
        left_child = right_tree.left_child
        while left_child.left_child is not None:
            left_child = left_child.left_child
        return left_child
    parent_of_node = node.parent
    while (parent_of_node is not None):
        if parent_of_node > node.value:
            return parent_of_node
        node = parent_of_node
        parent_of_node = node.parent
    return None



if __name__ == '__main__':
    values = [6, 44, 4, 8, 1, 3, 19, 2, 5]

    tree = Node()
    for value in values:
        insert(tree, value)
    print_tree(tree)
    delete(tree, 3)
    print('Tree after deleteing 3')
    print_tree(tree)
