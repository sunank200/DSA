class RecursionTree:
    def __init__(self):
        self.call: str = ""  # actual value of function call
        self.returned = None  # value returned from function
        self.children = []  # List[child]


def print_tree(node: RecursionTree = None, indent: str = ""):
    indent_size = 4
    if node is None or len(node.children) == 0:
        print(node.call + " returned: " + str(node.returned))
    else:
        print(node.call + " returned: " + str(node.returned))
        for child in node.children[:-1]:
            # here child node to parent
            print(indent + "|" + "-" * indent_size, end="")

            print_tree(child, indent + "|" + " " * indent_size)
        # last node in child
        child = node.children[-1]
        print(indent + "+" + "-" * indent_size, end="")
        print_tree(child, indent + " " * indent_size)
