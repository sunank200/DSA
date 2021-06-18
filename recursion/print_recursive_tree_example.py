"""
Given a staircase of n steps and a set of possible steps that we can climb at
a time named possibleSteps, create a function that returns the number of ways
a person can reach to the top of staircase.

Example:
    Input:
        n = 10
        possibleSteps = [2,4,5,8]
    Output: 11

    Explanation:
        [2,2,2,2,2], [2,2,2,4], [2,2,4,2], [2,4,2,2], [4,2,2,2], [4,4,2],
    [2,4,4], [4,2,4], [5,5], [8,2], [2,8]

    idea here is lets say if someone is at step 2, number of ways one can
    jump to step 10 is (10-2)->8 ways and similarly


    ways(10) = ways(10-2) + ways(10-4) + ways(10-5) + ways(10-8)
    i.e:
    ways(10) = ways(8) + ways(6) + ways(5) + ways(2)

    ways to jump to 10-2
                [2,2,2,2], [4,4] ,[2,2,4], [8], [2,4,2], [4,2,2]
"""


class RecursiveTree:
    def __init__(self):
        self.call: str = ""
        self.returned = None
        self.children = []


def print_tree(node: RecursiveTree, indent: str = ""):
    indent_size = 4
    if node is None or len(node.children) == 0:
        print(node.call + " returned: " + str(node.returned))
    else:
        print(node.call + " returned: " + str(node.returned))
        for child in node.children[:-1]:
            print(indent + "|" + "-" * indent_size, end="")
            print_tree(child, indent + "|" + " " * indent_size)

        child = node.children[-1]
        print(indent + "+" + "-" * indent_size, end="")
        print_tree(child, indent + "|" + " " * indent_size)


def ways_to_jump(stair, possible_steps, rt_node) -> int:
    rt_node.call = "ways_to_jump(" + str(stair) + ")"
    if stair == 0:  # only one way to jumping to step 0
        rt_node.returned = 1
        return 1
    no_of_ways = 0

    for steps in possible_steps:
        if stair - steps >= 0:
            child = RecursiveTree()
            rt_node.children.append(child)
            no_of_ways += ways_to_jump(stair - steps, possible_steps, child)
    rt_node.returned = no_of_ways
    return no_of_ways


if __name__ == "__main__":
    stairs = 10
    possible_steps = [2, 4, 5, 8]
    rt_node = RecursiveTree()
    print(ways_to_jump(10, possible_steps, rt_node))
    print_tree(rt_node, "")
