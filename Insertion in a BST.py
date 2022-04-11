class Node:
    left = right = None
    def __init__(self, data):
        self.data = data

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


def insert(root, key):

    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)

    return root

def constructBST(keys):
    root = None
    for key in keys:
        root = insert(root, key)
    return root


if __name__ == '__main__':
    keys = [15, 10, 20, 8, 12, 16, 25]

    root = constructBST(keys)
    inorder(root)