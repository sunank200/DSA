class MyCircularQueue:
    """
    head = 0
    tail = (head + count-1 ) % capacity
    """

    def __init__(self, k: int):
        self.c_queue = [None] * k
        self.head = 0
        self.capacity = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        self.c_queue[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.c_queue[self.head]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.c_queue[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.capacity == self.count


if __name__ == "__main__":
    obj = MyCircularQueue(10)
    obj.enQueue(1)
    obj.deQueue()
    obj.enQueue(-1)
    obj.enQueue(1)
    print(obj.Front())
    print(obj.Rear())
    print(obj.isEmpty())
    print(obj.isFull())
