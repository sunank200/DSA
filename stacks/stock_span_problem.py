"""
The stock span problem is a type of financial problem based on stocks where daily price of a stock is given.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and
going backwards) for which the price of the stock was less than or equal to today's price.

Example -
Input: [100, 80, 60, 70, 60, 75, 85]
Output: [1, 1, 1, 2, 1, 4, 6]

Input: [31, 27, 14, 21, 30, 22]
Output: [1, 1, 1, 2, 4, 1]
"""


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


def calculate_span(a, n):
    s = Stack()
    ngl_index = []
    for i in range(0, n, 1):
        if s.is_empty():
            ngl_index.append(-1)
        elif not s.is_empty() and a[i] < s.top()[0]:
            ngl_index.append(s.top()[1])
        elif not s.is_empty() and a[i] >= s.top()[0]:
            while not s.is_empty() and a[i] >= s.top()[0]:
                s.pop()
            if s.is_empty():
                ngl_index.append(-1)
            else:
                ngl_index.append(s.top()[1])
        s.push((a[i], i))
    result = []
    for index, ngl in enumerate(ngl_index):
        result.append(index - ngl)

    return result


def test_ssp():
    a_1 = [100, 80, 60, 70, 60, 75, 85]
    r_a_1 = [1, 1, 1, 2, 1, 4, 6]
    assert calculate_span(a_1, len(a_1)) == r_a_1, "Test case:1 failed."


if __name__ == "__main__":
    test_ssp()
