"""
Reverse a Stack in O(1) space using Recursion.

Example 1

Input: st = [1, 5, 3, 2, 4]
Output:[4, 2, 3, 5, 1]
Explanation: After reversing the stack [1, 5, 3, 2, 4]
becomes [4, 2, 3, 5, 1].
Example 2

Input: st = [5, 17, 100, 11]
Output: [11, 100, 17, 5]
Explanation: After reversing the stack [5, 17, 100, 11]
becomes [11, 100, 17, 5]
"""


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Underflow condition.")
        return self.stack.pop()

    def push(self, elm):
        self.stack.append(elm)

    def print_stack(self):
        print(self.stack)


def insert_at_bottom(s, tmp_emp):
    if s.is_empty():
        s.push(tmp_emp)
    else:
        current_top = s.top()
        s.pop()
        insert_at_bottom(s, tmp_emp)
        s.push(current_top)


def reverse_stack(s: Stack):
    if s.is_empty():
        return

    tmp_elm = s.top()
    s.pop()
    reverse_stack(s)
    insert_at_bottom(s, tmp_elm)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    s.print_stack()

    reverse_stack(s)

    s.print_stack()
