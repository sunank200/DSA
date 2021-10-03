"""
Given a knapsack weight W and a set of n items with certain value vali and
weight wti, we need to calculate the maximum amount that could make up this
quantity exactly. This is different from classical Knapsack problem, here we
are allowed to use unlimited number of instances of an item.
Examples:

Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}
Output : 110
We get maximum value with one unit of
weight 5 and one unit of weight 3.
"""


def unbounded_knapsack(weights, values, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    for i in range(len(weights) + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(weights)][capacity]


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [10, 40, 50, 70]
    capacity = 8
    print(unbounded_knapsack(weights, values, capacity))
