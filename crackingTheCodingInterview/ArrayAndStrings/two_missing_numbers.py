"""
Given an array of n unique integers where each element in the array is in the
range [1, n]. The array has all distinct elements and the size of the array
is (n-2). Hence Two numbers from the range are missing from this array.
Find the two missing numbers.
Examples :


Input  : arr[] = {1, 3, 5, 6}
Output : 2 4

Input : arr[] = {1, 2, 4}
Output : 3 5

Input : arr[] = {1, 2}
Output : 3 4

Approach:
    1. Calculate the sum of n natural numbers
    2. sum the arr
    3. sum of miising number = n_sum - c_sum
    4. avg = missing_sum/2
    5. calculate the sum of all number less or equal to the avg in arr
    -> sum_less_avg
    6. sum till avg -> avg_sum
    6. first = avg_sum - sum_less_avg
    7. second = missing sum - first
"""


def find_missing(arr):
    n = len(arr) + 2
    n_sum = (n * (n + 1)) // 2
    c_sum = sum(arr)
    missing_sum = n_sum - c_sum
    avg = missing_sum // 2
    sum_less_than_avg = 0
    for i in arr:
        if i <= avg:
            sum_less_than_avg += i
    avg_sum = (avg * (avg + 1)) // 2
    first = avg_sum - sum_less_than_avg
    second = missing_sum - first
    return [first, second]


def test_missing_two():
    test1 = [1, 3, 5, 6]
    assert find_missing(test1) == [2, 4], "Test case 1 failed."

    test2 = [1, 2, 4]
    assert find_missing(test2) == [3, 5], "Test 2 failed."

    test3 = [1, 2]
    assert find_missing(test3) == [3, 4], "Test 3 failed."


if __name__ == "__main__":
    test_missing_two()
