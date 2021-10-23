"""
Given a set of non-negative integers, and a value sum, determine if there is a
subset of the given set with sum equal to given sum.

Example:

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""


def subset_sum(arr, sum, n):
    dp = [[False for i in range(sum + 1)] for i in range(len(arr) + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for j in range(1, sum + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][sum]


def test():
    t1, s1 = [3, 34, 4, 12, 5, 2], 9
    assert subset_sum_practice(t1, s1, len(t1)) is True, "Test case 1 failed."

    t2, s2 = [35, 54, 100, 19, 39, 1, 89, 28, 68, 29, 94], 649
    assert subset_sum_practice(t2, s2, len(t2)) is True, "Test case 2 failed."


def subset_sum_practice(arr, sum, n):
    dp = [[False for i in range(sum + 1)] for i in range(len(arr) + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for j in range(1, sum + 1):
        dp[0][j] = False

    for i in range(n + 1):
        for j in range(sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][sum]


if __name__ == "__main__":
    test()
