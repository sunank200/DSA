"""
Given a value N, if we want to make change for N cents, and we have infinite
supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we
make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions:
 {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and
S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6},
{2,3,5} and {5,5}. So the output should be 5.

"""

# similar to count of subsets with sum equal to sum but unbounded


def coinchange2(coins, amount):
    dp = [[None for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for j in range(1, amount + 1):
        dp[0][j] = 0

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(coins)][amount] % 1000007


if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 4
    print(coinchange2(coins, sum))
