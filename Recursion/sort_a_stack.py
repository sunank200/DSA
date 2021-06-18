class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, elm):
        self.stack.append(elm)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow.")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def print_stack(self):
        print(self.stack)


def insert_in_stack(s, val):
    if s.is_empty() or s.top() < val:
        s.push(val)
    else:
        popped_value = s.pop()
        insert_in_stack(s, val)
        s.push(popped_value)


def sort_stack(s: Stack):
    if not s:
        return
    if not s.is_empty():
        topped_value = s.top()
        s.pop()
        sort_stack(s)
        insert_in_stack(s, topped_value)


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)

    # # before sorting
    s.print_stack()
    print("---------------")
    # after sorting
    sort_stack(s)

    s.print_stack()
