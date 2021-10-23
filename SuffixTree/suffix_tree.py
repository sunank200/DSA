"""
A suffix tree can be viewed as a data structure built
 on top of a trie where, instead of just adding the
 string itself
into the trie, you would also add every possible
suffix of that string. As an example, if you wanted
 to index the
string banana in a suffix tree, you would build a
trie with the following strings:

banana
anana
nana
ana
na
a
Once that's done you can search for any n-gram and see
if it is present in your indexed string. In other words,
 the n-gram search is a prefix search of all possible
 suffixes of your string.

This is the simplest and slowest way to build a suffix tree.
 It turns out that there are many fancier variants on
this data structure that improve on either or both space
and build time. I'm not well versed enough in this domain to
give an overview but you can start by looking into suffix
 arrays or this class advanced data structures.
"""


class TrieNode:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.is_end = False
        self.count = 0


class SuffixTree:
    def __init__(self, string):
        self.root = TrieNode("")
        self.populate_suffix_tree(string)

    def populate_suffix_tree(self, string):
        for i in range(len(string)):
            self.insert_sub_string_at_index(i, string)

    def insert_sub_string_at_index(self, i, string):
        node = self.root

        for j in range(i, len(string)):
            letter = string[j]
            # print(letter)
            if letter in node.children:
                node = node.children.get(letter)
            else:
                new_node = TrieNode(letter)
                node.children[letter] = new_node
                node = new_node
        node.is_end = True
        node.count += 0
        # print("------------")

    def contains(self, string):
        node = self.root
        print(string)
        for letter in string:
            if letter in node.children:
                node = node.children.get(letter)
            else:
                return False
        return True

    def print_suffix_tree(self):
        node = self.root

        queue = []
        queue.append(node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.key)
            for child in current_node.children:
                queue.append(current_node.children[child])


def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    """
    Use suffix tree to store big string
    """
    suffix_tree = SuffixTree(bigString)

    # suffix_tree.print_suffix_tree()
    result = []
    for word in smallStrings:
        result.append(suffix_tree.contains(word))

    return result


if __name__ == "__main__":
    print(
        multiStringSearch(
            "this is a big string",
            ["this", "yo", "is", "a", "bigger", "string", "kappa"],
        )
    )
