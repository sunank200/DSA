class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.stack.pop()

    def push(self, elm):
        self.stack.append(elm)

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]


def next_smaller(arr):
    arr_size = len(arr)
    s = Stack()
    result = []
    for i in range(arr_size - 1, -1, -1):
        if s.is_empty():
            result.append(-1)
        elif not s.is_empty() and arr[i] > s.top():
            result.append(s.top())
        elif not s.is_empty() and arr[i] <= s.top():
            while not s.is_empty() and arr[i] <= s.top():
                s.pop()
            if s.is_empty():
                result.append(-1)
            else:
                result.append(s.top())
        s.push(arr[i])
    result.reverse()
    return result


def test_nsr():
    a_1 = [4, 8, 5, 2, 25]
    r_a_1 = [2, 5, 2, -1, -1]
    assert next_smaller(a_1) == r_a_1, "Test case: 1 failed."

    a_2 = [1, 6, 4, 10, 2, 5]
    r_a_2 = [-1, 4, 2, 2, -1, -1]
    assert next_smaller(a_2) == r_a_2, "Test case: 2 failed."


if __name__ == "__main__":
    test_nsr()
