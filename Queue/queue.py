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

    def top(self):
        if self.is_empty():
            return None
        return self.q[0]

    def size(self):
        return len(self.q)

    def print_queue(self):
        return self.q


def test():
    a = Queue()
    a.enqueue(10)
    a.enqueue(-12)
    assert a.print_queue() == [10, -12], "Test case 1 failed."

    assert a.top() == 10, "Test case 2 failed."
    a.dequeue()

    assert a.top() == -12, "Test case 3 failed."


if __name__ == "__main__":
    test()
