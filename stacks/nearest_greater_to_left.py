class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, elm):
        self.stack.append(elm)

    def top(self):
        if self.is_empty():
            return None
        return self.stack[len(self.stack) - 1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.stack.pop()


def next_greater_element_on_left(arr):
    arr_size = len(arr)
    s = Stack()
    result = []
    for i in range(0, arr_size):
        if s.is_empty():
            result.append(-1)
        elif not s.is_empty() and arr[i] < s.top():
            result.append(s.top())
        elif not s.is_empty() and arr[i] >= s.top():
            while not s.is_empty() and arr[i] >= s.top():
                s.pop()
            if s.is_empty():
                result.append(-1)
            else:
                result.append(s.top())
        s.push(arr[i])
    return result


def test_ngl():
    arr_1 = [1, 3, 2, 4]
    rarr_1 = [-1, -1, 3, -1]
    assert next_greater_element_on_left(arr_1) == rarr_1, "Test case:1 failed."

    arr_2 = [11, 6, 42, 65, 32, 54]
    assert next_greater_element_on_left(arr_2) == [
        -1,
        11,
        -1,
        -1,
        65,
        65,
    ], "Test case:2 failed."

    arr_3 = [40, 50, 20, 10, 60]
    assert next_greater_element_on_left(arr_3) == [
        -1,
        -1,
        50,
        20,
        -1,
    ], "Test case: 3 failed."


if __name__ == "__main__":
    test_ngl()
