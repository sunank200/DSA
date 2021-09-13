"""
Given an array arr[] of length N and an integer X, the task is to find the
number of subsets with a sum equal to X.

Examples:

Input: arr[] = {1, 2, 3, 3}, X = 6
Output: 3
All the possible subsets are {1, 2, 3},
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1
Output: 4
"""


def count_subsets_with_sum(arr, sum):
    dp = [[False for _ in range(sum + 1)] for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        dp[i][0] = 1

    for j in range(1, sum + 1):
        dp[0][j] = 0

    for i in range(1, len(arr) + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(arr)][sum]


def test():
    t1, s1 = [1, 2, 3, 3], 6
    assert count_subsets_with_sum(t1, s1) == 3, "Testcase 1 failed."

    t2, s2 = [1, 1, 1, 1], 1
    assert count_subsets_with_sum(t2, s2) == 4, "Testcase 2 failed."


if __name__ == "__main__":
    test()
