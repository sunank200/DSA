class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elm):
        self.stack.append(elm)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]


def prev_smaller(a):
    a_size = len(a)
    s = Stack()
    result = []
    for i in range(0, a_size):
        if s.is_empty():
            result.append(-1)
        elif not s.is_empty() and a[i] > s.top():
            result.append(s.top())
        elif not s.is_empty() and a[i] <= s.top():
            while not s.is_empty() and a[i] <= s.top():
                s.pop()
            if s.is_empty():
                result.append(-1)
            else:
                result.append(s.top())
        s.push(a[i])
    return result


def test_nsl():
    a_1 = [1, 6, 4, 10, 2, 5]
    r_a_1 = [-1, 1, 1, 4, 1, 2]
    assert prev_smaller(a_1) == r_a_1, "Test case:1 failed."

    a_2 = [1, 3, 0, 2, 5]
    r_a_2 = [-1, 1, -1, 0, 2]
    assert prev_smaller(a_2) == r_a_2, "Test case:2 failed."


if __name__ == "__main__":
    test_nsl()
