class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack being poped is empty.")
        return self.stack.pop()

    def push(self, num):
        self.stack.append(num)


def next_larger_element(arr, n):
    s = Stack()
    answer = []
    for i in range(n - 1, -1, -1):
        if s.is_empty():
            answer.append(-1)
        elif not s.is_empty() and arr[i] < s.top():
            answer.append(s.top())
        elif not s.is_empty() and arr[i] >= s.top():
            while not s.is_empty() and arr[i] >= s.top():
                s.pop()
            if s.is_empty():
                answer.append(-1)
            else:
                answer.append(s.top())
        s.push(arr[i])

    answer.reverse()
    return answer

def test_ngr():
    arr1 = [1, 3, 2, 4]
    assert next_larger_element(arr1,len(arr1)) == [3, 4, 4, -1], "Test case 1 failed."

if __name__ == "__main__":
    test_ngr()
    arr = [1,3,0,0,1,2,4]
    print(next_larger_element(arr,len(arr)))
