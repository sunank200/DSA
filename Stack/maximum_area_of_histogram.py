"""Problem Find the largest rectangular area possible in a given histogram
where the largest rectangle can be made of a number of contiguous bars.
Assume that all bars have same width and the width is 1 unit.

Given n non-negative integers representing the histogram's bar height where
the width of each bar is 1, find the area of largest rectangle in the
histogram.

This is what we have to calculate.

Example -
Input: [2, 1, 5, 6, 2, 3]
Output: 10

Input: [6, 2, 5, 4, 5, 1, 6]
Output: 12
"""


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, elm):
        return self.stack.append(elm)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow.")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]


def nearest_smaller_to_right_index(heights):
    nsr_stack = Stack()
    nsr = []
    height_size = len(heights)
    for i in range(height_size - 1, -1, -1):
        if nsr_stack.is_empty():
            nsr.append(height_size)
        elif not nsr_stack.is_empty() and heights[i] > nsr_stack.top()[0]:
            nsr.append(nsr_stack.top()[1])
        elif not nsr_stack.is_empty() and heights[i] <= nsr_stack.top()[0]:
            while not nsr_stack.is_empty() and heights[i] <= nsr_stack.top()[0]:
                nsr_stack.pop()
            if nsr_stack.is_empty():
                nsr.append(height_size)
            else:
                nsr.append(nsr_stack.top()[1])
        nsr_stack.push((heights[i], i))
    nsr.reverse()
    return nsr


def nearest_smaller_to_left_index(heights):
    nsl_stack = Stack()
    nsl = []
    height_size = len(heights)
    for i in range(0, height_size):
        if nsl_stack.is_empty():
            nsl.append(-1)
        elif not nsl_stack.is_empty() and heights[i] > nsl_stack.top()[0]:
            nsl.append(nsl_stack.top()[1])
        elif not nsl_stack.is_empty() and heights[i] <= nsl_stack.top()[0]:
            while not nsl_stack.is_empty() and heights[i] <= nsl_stack.top()[0]:
                nsl_stack.pop()
            if nsl_stack.is_empty():
                nsl.append(-1)
            else:
                nsl.append(nsl_stack.top()[1])
        nsl_stack.push((heights[i], i))
    return nsl


def largest_rectangle_area(heights):
    # calculate nearest_smaller_to_right_index : nsr_index
    # calculate nearest_smaller_to_left_index : nsl_index
    # width = nsr_index - nsl_index -1
    # area [i] = heights[i] * width
    nsl_index = nearest_smaller_to_left_index(heights)
    nsr_index = nearest_smaller_to_right_index(heights)

    max_area = -1
    for i in range(0, len(heights)):
        area = heights[i] * (nsr_index[i] - nsl_index[i] - 1)
        if max_area < area:
            max_area = area
    return max_area


def test_mah():
    a_1 = [2, 1, 5, 6, 2, 3]
    assert largest_rectangle_area(a_1) == 10, "Test case:1 failed."

    a_2 = [2, 4]
    assert largest_rectangle_area(a_2) == 4, "Test case:2 failed."

    a_3 = [6, 2, 5, 4, 5, 1, 6]
    assert largest_rectangle_area(a_3) == 12, "Test case:3 failed."

    a_4 = [0, 1, 1, 0]
    assert largest_rectangle_area(a_4) == 2, "Test case:4 failed."


if __name__ == "__main__":
    test_mah()
