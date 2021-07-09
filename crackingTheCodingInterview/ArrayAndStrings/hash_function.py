"""
Hash Function or hash table
Hashing is a data structure that is used to store a large amount of data,
which can be accessed in O(1) time by operations such as search, insert
and delete.

hash_code = hash(key) % len(hash_table)

Collision resolution:
A collision occurs when two items/values get the same slot/index, i.e. the
hashing function generates same slot number for multiple items. If proper
collision resolution steps are not taken then the previous item in the slot
will be replaced by the new item whenever the collision occurs.

1. Linear probing
One way to resolve collision is to find another open slot whenever there is
a collision and store the item in that open slot. The search for open slot
starts from the slot where the collision happened. It moves sequentially
through the slots until an empty slot is encountered. The movement is in a
circular fashion. It can move to the first slot while searching for an empty
slot. Hence, covering the entire hash table. This kind of sequential search
is called Linear Probing.

2. Chaining
The other way to resolve collision is Chaining. This allows multiple items
exist in the same slot/index. This can create a chain/collection of items
in a single slot. When the collision happens, the item is stored in the same
slot using chaining mechanism.
"""
INITIAL_CAPACITY = 10


class HashTable:
    def __init__(self):
        self.hash_table = [[] for _ in range(INITIAL_CAPACITY)]

    def hash_function(self, key):
        return hash(key) % len(self.hash_table)

    def search(self, key):
        _hashed_key = self.hash_function(key)
        bucket = self.hash_table[_hashed_key]
        for i, key_value in enumerate(bucket):
            k, v = key_value
            if key == k:
                return v
        return None

    def insert(self, key, value):
        _hashed_key = self.hash_function(key)
        bucket = self.hash_table[_hashed_key]
        if self.search(key) is None:
            # append the (key, value) if it doesn't exists
            bucket.append((key, value))
        else:
            # replace the (key, value) if it exists
            for index, key_val in enumerate(bucket):
                k, v = key_val
                if k == key:
                    bucket[index] = (key, value)

    def delete(self, key):
        if self.search(key):
            # delete it
            _hashed_key = self.hash_function(key)
            bucket = self.hash_table[_hashed_key]
            for i, key_value in enumerate(bucket):
                k, v = key_value
                if key == k:
                    bucket.pop(i)
                    print("Key {} deleted.".format(key))
                    return True
        else:
            print("key {} not found".format(key))
            return False

    def print_hash_table(self):
        print(self.hash_table)


def test_hash():
    test_set = [
        (10, "India"),
        ("10", "Nepal"),
        ("Nepal", 10),
        ("", "123"),
        (12334, "ABC"),
    ]

    hash_obj = HashTable()
    for key, value in test_set:
        hash_obj.insert(key, value)

    hash_obj.print_hash_table()

    assert hash_obj.search("10") == "Nepal", "Search Failed."

    assert hash_obj.delete("10") is True, " Delete Failed"
    hash_obj.print_hash_table()

    assert hash_obj.delete("10") is False, "Delete failed"

    hash_obj.insert(10, "China")
    hash_obj.print_hash_table()


if __name__ == "__main__":
    test_hash()
