"""
Trie(PrefixTree) or prefix tree is an n-ary tree in which characters
are stored at each node. Each path down the tree represents
a word.
"""


class TrieNode:
    def __init__(self, ch: str):
        # dictionary of child nodes, key are characters and
        # value are node.
        self.children = {}

        # the character stored in this node
        self.key = ch

        # counter indicating how many times word is inserted
        # to trie
        self.count = 0

        # whether it is a complete word
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children.get(char)
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True
        node.count += 1

    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.key, node.count))
        for child in node.children.values():
            self.dfs(child, prefix + node.key)

    def query(self, prefix):
        """
        Given a prefix return all the words which start with prefix
        and return the list of word in sorted order by number of time,
        they have been inserted.
        :param prefix:
        :return:
        """
        self.output = []
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children.get(char)
            else:
                return self.output

        self.dfs(node, prefix[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def find(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children.get(char)
            else:
                return False, word, 0
        if node.is_end:
            return True, word, node.count
        return False, word, 0

    def delete(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children.get(char)
            else:
                return "{} not found".format(word)

        if node.is_end:
            node.count -= 1
            return "{} deleted.".format(word)
        return "{} not found".format(word)


if __name__ == "__main__":
    trie_obj = Trie()
    trie_obj.insert("was")
    trie_obj.insert("wax")
    trie_obj.insert("what")
    trie_obj.insert("word")
    trie_obj.insert("work")
    trie_obj.insert("won")
    trie_obj.insert("was")
    trie_obj.insert("waxing")
    trie_obj.insert("wax")
    trie_obj.insert("wax")

    print(trie_obj.query("wa"))
    print(trie_obj.find("wa"))
    print(trie_obj.delete("was"))
    print(trie_obj.query("wa"))
