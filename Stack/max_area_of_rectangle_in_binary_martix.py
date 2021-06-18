"""Given a binary matrix. Find the maximum area of a rectangle formed only
of 1s in the given matrix.

Example 1:

Input: n = 4, m = 4 M[][] = {{0 1 1 0}, {1 1 1 1}, {1 1 1 1}, {1 1 0 0}}
Output: 8 Explanation: For the above test case the matrix will look like 0 1
1 0 1 1 1 1 1 1 1 1 1 1 0 0 the max size rectangle is 1 1 1 1 1 1 1 1 and
area is 4 *2 = 8. Your Task: Your task is to complete the function maxArea
which returns the maximum size rectangle area in a binary-sub-matrix with
all 1’s. The function takes 3 arguments the first argument is the Matrix M[
] [ ] and the next two are two integers n and m which denotes the size of
the matrix M.

Expected Time Complexity : O(n*m)
Expected Auixiliary Space : O(m)

Constraints:
1<=n,m<=1000
0<=M[][]<=1

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


def compute_nsr_index(arr):
    s_r = Stack()
    arr_size = len(arr)

    result = []
    for i in range(arr_size - 1, -1, -1):
        if s_r.is_empty():
            result.append(arr_size)
        elif not s_r.is_empty() and arr[i] > s_r.top()[0]:
            result.append(s_r.top()[1])
        elif not s_r.is_empty() and arr[i] <= s_r.top()[0]:
            while not s_r.is_empty() and arr[i] <= s_r.top()[0]:
                s_r.pop()
            if s_r.is_empty():
                result.append(arr_size)
            else:
                result.append(s_r.top()[1])
        s_r.push((arr[i], i))
    res = []
    for i in range(len(result) - 1, -1, -1):
        res.append(result[i])
    return res


def compute_nsl_index(arr):
    s = Stack()
    arr_size = len(arr)
    result = []

    for i in range(0, arr_size):
        if s.is_empty():
            result.append(-1)
        elif not s.is_empty() and arr[i] > s.top()[0]:
            result.append(s.top()[1])
        elif not s.is_empty() and arr[i] <= s.top()[0]:
            while not s.is_empty() and arr[i] <= s.top()[0]:
                s.pop()
            if s.is_empty():
                result.append(-1)
            else:
                result.append(s.top()[1])
        s.push((arr[i], i))
    return result


def calculate_maximum_area_of_histogram(arr):
    # compute nsr_index
    # compute nsl_index
    # width = nsr_index - nsl_index - 1
    arr_size = len(arr)
    nsr_index = compute_nsr_index(arr)
    nsl_index = compute_nsl_index(arr)
    max_area = -1
    for i in range(0, arr_size):
        area = arr[i] * (nsr_index[i] - nsl_index[i] - 1)
        if max_area < area:
            max_area = area
    return max_area


def max_area(M, n, m):
    """
    max_area returns maximum area of the rectange.
    :param M: 2d matix
    :param n: rows
    :param m: columns
    :return: maximum area
    """
    # make 4 histograms and compute maximum area of histogram.
    # max area of all is result.
    histograms = []
    for i in range(0, n):
        histo = []
        if i == 0:
            histo = M[i]
        else:
            for j in range(0, m):
                if M[i][j] == 0:
                    histo.append(0)
                else:
                    histo.append(histograms[i - 1][j] + M[i][j])
        histograms.append(histo)

    max_area = 0
    for i in range(0, len(histograms)):
        area = calculate_maximum_area_of_histogram(histograms[i])
        if max_area < area:
            max_area = area
    return max_area


def test_max_area():
    a_1 = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
    assert max_area(a_1, 4, 4) == 8, "Test case:1 failed."


if __name__ == "__main__":
    test_max_area()
