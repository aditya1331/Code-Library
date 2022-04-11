# Data structure to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to find the size of the maximum independent set
# for a binary tree
def findMISSize(root):
    # base case: empty tree
    if root is None:
        return 0

    # Case 1: Exclude the current node from the maximum independent set and
    # recur for its left and right child
    excl = findMISSize(root.left) + findMISSize(root.right)

    # Case 2: Include the current node in the maximum independent set and
    # recur for its grandchildren
    incl = 1

    if root.left:
        incl += findMISSize(root.left.left) + findMISSize(root.left.right)

    if root.right:
        incl += findMISSize(root.right.left) + findMISSize(root.right.right)

    # return the maximum number of nodes possible by either
    # including or excluding the current node
    return max(excl, incl)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    print('The size of a maximum independent set is', findMISSize(root))