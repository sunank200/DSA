# print height of binary tree
"""
1
| |
2   3
| |
4   5
|
6
|
7
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def compute_height(bt: BinaryTree):
    if bt is None:
        return 0

    return 1 + max(compute_height(bt.left), compute_height(bt.right))


if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.left = BinaryTree(2)
    bt.right = BinaryTree(3)
    bt.left.left = BinaryTree(4)
    bt.left.right = BinaryTree(5)
    bt.left.left.left = BinaryTree(6)
    bt.left.left.left.left = BinaryTree(7)

    print(compute_height(bt))
