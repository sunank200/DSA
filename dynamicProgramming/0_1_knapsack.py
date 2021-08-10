"""
Given weights and values of n items, put these items in a knapsack
of capacity W to get the maximum total value in the knapsack. In
other words, given two integer arrays val[0..n-1] and wt[0..n-1]
which represent values and weights associated with n items respectively.
Also given an integer W which represents knapsack capacity, find out the
maximum value subset of val[] such that sum of the weights of this subset
is smaller than or equal to W. You cannot break an item, either pick
the complete item or don’t pick it (0-1 property).

Input:
    wt = [1,3,4,5]
    val = [1,4,5,7]

    Capacity - W = 7kg
"""


def knapsack_recursive(wt, val, W, n):
    if n == 0 or W == 0:
        return 0

    # if weight of nth item is greater than knapsack, it cannot be included
    if wt[n - 1] > W:
        return knapsack_recursive(wt, val, W, n - 1)

    else:
        # maximum value if we include item or exlude item
        return max(
            val[n - 1] + knapsack_recursive(wt, val, W - wt[n - 1], n - 1),
            knapsack_recursive(wt, val, W, n - 1),
        )


def knapsack_memoize(wt, val, W, n, dp):
    if W == 0 or n == 0:
        return 0

    if dp[n][W] is not None:
        return dp[n][W]

    if wt[n - 1] <= W:
        dp[n][W] = max(
            val[n - 1] + knapsack_memoize(wt, val, W - wt[n - 1], n - 1, dp),
            knapsack_memoize(wt, val, W, n - 1, dp),
        )
        return dp[n][W]
    else:
        dp[n][W] = knapsack_memoize(wt, val, W, n - 1, dp)
        return dp[n][W]


def knapsack_top_down(wt, val, W, n, dp):
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0  # base condition above returned 0
    # print(dp)
    for i in range(n + 1):
        for j in range(W + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


def test():
    wt = [1, 3, 4, 5]
    val = [1, 4, 5, 7]

    W = 7
    assert knapsack_recursive(wt, val, W, 4) == 9, "Test case 1 failed."

    dp = [[None] * (W + 1)] * ((len(wt) + 1))
    assert knapsack_memoize(wt, val, W, len(wt), dp) == 9, "Test case 2 failed."

    dp = [[None] * (W + 1)] * ((len(wt) + 1))
    assert knapsack_top_down(wt, val, W, len(wt), dp) == 9, "Test case 3 failed."


if __name__ == "__main__":
    test()
