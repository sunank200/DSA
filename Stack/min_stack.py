"""
Design a stack that supports push, pop, top, and retrieving the
minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

"""


class MinStack:
    def __init__(self):
        self.s = []
        self.min_val = None

    def is_empty(self):
        return len(self.s) == 0

    def push(self, elm):
        if self.is_empty():
            self.s.append(elm)
            self.min_val = elm
            return

        if elm < self.min_val:
            self.s.append(2 * elm - self.min_val)
            self.min_val = elm
        else:
            self.s.append(elm)

        return

    def pop(self):
        if self.is_empty():
            return None

        removed_val = self.s[-1]
        self.s.pop()

        if self.min_val > removed_val:
            self.min_val = 2 * self.min_val - removed_val
        return

    def top(self):
        if self.is_empty():
            return None

        if self.min_val > self.s[-1]:
            return self.min_val
        else:
            return self.s[-1]

    def get_min(self):
        if self.is_empty():
            return None
        return self.min_val


def test():
    ss = MinStack()
    ss.push(-2)
    ss.push(0)
    ss.push(-3)
    assert ss.get_min() == -3, "Test case 1 failed."

    ss.pop()
    assert ss.top() == 0, "Test case 2 failed."
    assert ss.get_min() == -2, "Test case 3 failed."


if __name__ == "__main__":
    test()
