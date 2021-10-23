"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other
words, it is the product of some integer with itself. For example, 1, 4, 9,
and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:

1 <= n <= 104
"""
import math


def perfect_square_dp_1(n):
    """
    TC: O(n.sqrt(n)
     SC: O(n.sqrt(n)
    """
    square_nums = [i * i for i in range(1, int(math.sqrt(n)) + 1)]

    amount = n

    dp = [[float("inf") for _ in range(n + 1)] for _ in range(len(square_nums) + 1)]

    # make first column 0 - with square_nums = [], minimum perfect sqaure to make sum 0
    for i in range(1, len(square_nums) + 1):
        dp[i][0] = 0

    for i in range(1, len(square_nums) + 1):
        for j in range(1, n + 1):
            if square_nums[i - 1] <= j:
                dp[i][j] = min(1 + dp[i][j - square_nums[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(square_nums)][n]


def perfect_square_better_2(n):
    """
    TC: O(n.sqrt(n)
    SC: O(n)
    :param n:
    :return:
    """
    square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

    dp = [float("inf")] * (n + 1)
    # bottom case
    dp[0] = 0

    for i in range(1, n + 1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)

    return dp[-1]


if __name__ == "__main__":
    print(perfect_square_dp_1(12))
    print(perfect_square_better_2(15))
