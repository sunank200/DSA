"""
Given a rod of length n inches and an array of prices that includes prices of
all pieces of size smaller than n. Determine the maximum value obtainable by
cutting up the rod and selling the pieces. For example, if the length of the
rod is 8 and the values of different pieces are given as the following, then
the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and
6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24
(by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""


def rod_cutting_problem(lengths, prices, max_length):
    dp = [[0 for _ in range(max_length + 1)] for _ in range(len(lengths) + 1)]

    for i in range(len(lengths) + 1):
        for j in range(max_length + 1):
            if lengths[i - 1] <= j:
                dp[i][j] = max(prices[i - 1] + dp[i][j - lengths[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(lengths)][max_length]


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    lengths = [i for i in range(1, len(prices) + 1)]

    max_length = 8
    print(rod_cutting_problem(lengths, prices, max_length))
