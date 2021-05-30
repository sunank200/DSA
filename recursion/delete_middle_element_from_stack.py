"""
Delete middle element of a stack

Given a stack with push(), pop(), empty() operations, delete middle of
it without using any additional data structure.

Input  : Stack[] = [1, 2, 3, 4, 5]
Output : Stack[] = [1, 2, 4, 5]

Input  : Stack[] = [1, 2, 3, 4, 5, 6]
Output : Stack[] = [1, 2, 4, 5, 6]
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
            raise Exception("Underflow condtion.")
        return self.stack.pop()

    def push(self, elm):
        self.stack.append(elm)

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)


def delete_middle_element(s: Stack, n, current_element):
    # traverse the stack till middle element and pop
    # push everything apart from middle element from stack frame
    # if s.is_empty() or current_element == n:
    #     return
    #
    # temp_elm = s.top()
    # s.pop()
    #
    # delete_middle_element(s, n,current_element+1)
    #
    # if current_element != n//2:
    #     s.push(temp_elm)

    if s.is_empty():
        return

    if current_element == n // 2:
        s.pop()

    temp_elm = s.top()
    s.pop()
    delete_middle_element(s, n, current_element + 1)

    s.push(temp_elm)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print("before")
    print(s.print_stack())
    delete_middle_element(s, s.size(), 0)

    print("after")
    print(s.print_stack())

    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.push(5)
    s1.push(6)
    print("--before--")
    print(s1.print_stack())
    delete_middle_element(s1, s.size(), 0)

    print("after")
    print(s1.print_stack())
