"""
Implement a last in first out (LIFO) stack using only two queues. The
implemented stack should support all the functions of a normal queue (push,
top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means only push to
back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may
simulate a queue using a list or deque (double-ended queue), as long as you
use only a queue's standard operations.

"""


class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, elm):
        self.q.append(elm)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self.q.pop(0)

    def size(self):
        return len(self.q)

    def peek(self):
        if self.is_empty():
            return None
        return self.q[0]


class MyStack:
    """
    two queue: push -> O(1) and pop --> O(n)
    q1, q2
    push -> enqueue q1
    pop -> dequeue q1 till size of queue is 1 and enqueue to q2, when 1
    dequeue it
            q1 = q2

    one queue: push -> O(n) and pop-> O(1)
    q1
    push:  enqueue elm, deqeueue each element add enqueue to q1 for
    q1.size()-1:
    pop: dequeue
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.enqueue(x)
        _size = self.q1.size()

        while _size > 1:
            self.q1.enqueue(self.q1.dequeue())
            _size -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1.is_empty():
            return -1
        return self.q1.dequeue()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1.is_empty():
            return -1
        return self.q1.peek()

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.is_empty()


def test_stack():
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2, "Top failed."

    s.pop()
    assert s.top() == 1, "Pop failed."

    assert s.empty() is False, "Empty failed "


if __name__ == "__main__":
    test_stack()
