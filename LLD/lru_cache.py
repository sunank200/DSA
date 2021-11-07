# from collections import OrderedDict  # it uses double linked list inside of it
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.max_size = capacity
#         self.current_size = 0
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             val = self.cache[key]
#             self.cache.move_to_end(key)
#             return val
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache[key] = value
#             self.cache.move_to_end(key)
#             return
#         if self.current_size >= self.max_size:
#             self.cache.popitem(last=False)  # last=False sets FIFO like pop
#             self.current_size -= 1
#         self.cache[key] = value
#         self.current_size += 1


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head_to(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_binding()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def remove_tail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def remove_binding(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.current_size = 0
        self.list_of_most_recent = DoublyLinkedList()


def insertKeyValuePair(self, key, value):
    # Write your code here.
    if key not in self.cache:
        if self.current_size >= self.maxSize:
            self.remove_least_recently_used()
        else:
            self.current_size += 1
        self.cache[key] = DoublyLinkedListNode(key, value)
    else:
        self.replace_key(key, value)
    self.update_most_recent(self.cache[key])


def getValueFromKey(self, key):
    # Write your code here.
    if key not in self.cache:
        return None
    self.update_most_recent(self.cache[key])
    return self.cache[key].val


def getMostRecentKey(self):
    # Write your code here.
    if self.list_of_most_recent.head is None:
        return None
    return self.list_of_most_recent.head.key

    def remove_least_recently_used(self):
        key_to_remove = self.list_of_most_recent.tail.key
        self.list_of_most_recent.remove_tail()
        del self.cache[key_to_remove]

    def update_most_recent(self, node):
        self.list_of_most_recent.set_head_to(node)

    def replace_key(self, key, val):
        if key not in self.cache:
            raise Exception("Key not found.")
        self.cache[key].val = val
