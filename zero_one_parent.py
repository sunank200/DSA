# Suppose we have some input data describing a graph of relationships between
# parents and children over multiple families and generations. The data is
# formatted as a list of (parent, child) pairs, where each individual is
# assigned a unique positive integer identifier.

# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

# 1   2    4           30
#  \ /   /  \           \
#   3   5    9  15      16
#    \ / \    \ /
#     6   7   12


# Sample input/output (pseudodata):

# parentChildPairs = [
#     (3, 6), (1, 3), (2, 3), (5, 6), (15, 12),
#     (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
# ]


# Write a function that takes this data as input and returns two
# collections: one containing all individuals with zero known parents, and
# one containing all individuals with exactly one known parent.


# Output may be in any order:

# findNodesWithZeroAndOneParents(parentChildPairs) => [
#   [1, 2, 4, 15, 30],   // Individuals with zero parents
#   [5, 7, 9, 16]        // Individuals with exactly one parent
# ]

# Complexity Analysis variables:

# n: number of pairs in the input

# 3 -> 6
# 1 -> 3
# 2 -> 3
# 5 -> 6, 7
# 15 -> 12
# 4 -> 5, 9
# 9 -> 12
# 30 ->16

parent_child_pairs = [
    (3, 6),
    (1, 3),
    (2, 3),
    (5, 6),
    (15, 12),
    (5, 7),
    (4, 5),
    (4, 9),
    (9, 12),
    (30, 16),
]


def parents_exists(parent, occurnace_dict):
    occ = 0
    for key, val in occurnace_dict.items():
        if parent in val:
            occ += 1

    return occ == 0, occ == 1


def findNodesWithZeroAndOneParents(parent_child_pairs):
    zero_parents = set()
    one_parents = set()

    each_node = set()
    occurnace_dict = {}
    # create a dict with occurance
    for parent, child in parent_child_pairs:
        each_node.add(parent)
        each_node.add(child)
        if parent in occurnace_dict:
            temp = occurnace_dict.get(parent)
            temp.append(child)
        else:
            occurnace_dict[parent] = [child]

    for node in each_node:
        zero_pa, one_pa = parents_exists(node, occurnace_dict)
        if zero_pa:
            zero_parents.add(node)
        elif one_pa:
            one_parents.add(node)

    return zero_parents, one_parents


if __name__ == "__main__":
    print(findNodesWithZeroAndOneParents(parent_child_pairs))
