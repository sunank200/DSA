"""
You are given an integer array coins representing coins of different
 denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
 amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
"""


def minimum_coins(coins, sum):
    if len(coins) == 0:
        return -1
    # initialization
    dp = [[float("inf") for _ in range(sum + 1)] for _ in range(len(coins) + 1)]

    # # make first row INT_MAX
    # for j in range(sum+1):
    #     dp[0][j] = float('inf')

    # make first col 0 execpt 0,0
    for i in range(1, len(coins) + 1):
        dp[i][0] = 0

    i = 1
    # second row, if j % coin[0] == 0, make j//coin[0] else INT_MAX
    # for j in range(1, sum+1):
    #     if j % coins[0] == 0:
    #         dp[i][j] = j//coins[0]
    #     else:
    #         dp[i][j] = float('inf')

    for i in range(1, len(coins) + 1):
        for j in range(1, sum + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(coins)][sum] if dp[len(coins)][sum] != float("inf") else -1


if __name__ == "__main__":
    coins = [2]
    sums = 3
    print(minimum_coins(coins, sums))
