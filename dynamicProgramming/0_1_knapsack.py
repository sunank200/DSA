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


def test():
    wt = [1, 3, 4, 5]
    val = [1, 4, 5, 7]

    W = 7
    assert knapsack_recursive(wt, val, W, 4) == 9, "Test case 1 failed."


if __name__ == "__main__":
    test()
