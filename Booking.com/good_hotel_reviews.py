"""
Problem Description

Given a set of reviews provided by the customers for different hotels and a
string containing Good Words, you need to sort the reviews in descending order
according to their Goodness Value (Higher goodness value first). We define the
 Goodness Value of a string as the number of Good Words in that string.

NOTE: Sorting should be stable. If review i and review j have the same
Goodness Value then their original order would be preserved.

You are expected to use Trie in an Interview for such problems



Problem Constraints
1 <= No.of reviews <= 200
1 <= No. of words in a review <= 1000
1 <= Length of an individual review <= 10,000
1 <= Number of Good Words <= 10,000
1 <= Length of an individual Good Word <= 4
All the alphabets are lower case (a - z)


Input Format
First argument is a string A containing "Good Words" separated by "_" character

Second argument is a vector B of strings containing Hotel Reviews. Review
strings are also separated by "_" character.



Output Format
Return a vector of integers which contain the original indexes of the reviews
in the sorted order of reviews.



Example Input
Input 1:

 A = "cool_ice_wifi"
 B = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]


Example Output
Output 1:

 [2, 0, 1]


Example Explanation
Explanation 1:

 sorted reviews are ["cool_wifi_speed", "water_is_cool", "cold_ice_drink"]

"""


class TrieNode:
    def __init__(self, ch):
        self.key = ch
        self.children = {}
        self.count = 0
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch in node.children:
                node = node.children.get(ch)
            else:
                new_node = TrieNode(ch)
                node.children[ch] = new_node
                node = new_node
        node.is_end = True
        node.count += 1

    def find(self, word):
        node = self.root

        for ch in word:
            if ch in node.children:
                node = node.children.get(ch)
            else:
                return False
        if node.is_end:
            return True
        return False


def good_hotel_review(A, B):
    good_words = A.split("_")

    good_words_trie = Trie()
    for word in good_words:
        good_words_trie.insert(word)

    review_good_count = []
    for index, review in enumerate(B):
        review_words = review.split("_")

        count = 0
        for word in review_words:
            if good_words_trie.find(word):
                count += 1
        review_good_count.append((index, count))

    review_good_count.sort(key=lambda x: x[1], reverse=True)

    result = []
    for elm in review_good_count:
        result.append(elm[0])

    return result


if __name__ == "__main__":
    A = "cool_ice_wifi"
    B = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
    print(good_hotel_review(A, B))
