"""
A robot is located at the top-left corner of a m x n grid (marked 'Start'
 in the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?

Input: m = 3, n = 7
Output: 28
"""


def uniquePaths(m: int, n: int) -> int:
    """
    1. In first row, there is only one path to cells... right --> right so 1 ways to reach those cells.
    2. In first cols, there is only one way to reach ... down ---> down so 1 way to each those cells.
    3. for inner cells unique_path(1,1) = unique_path(0,1) + unique_path(1,0)

    4. dp based solution:
        a. initialize first row to 1 and first col to 1
        b. in for loop
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        c. return dp[m][n]
    """

    dp = [[None for _ in range(n)] for _ in range(m)]

    for i in range(m):
        dp[i][0] = 1

    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

    # DP Solution


#         if m == 1 or n == 1:
#             return 1

#         # O(n) Space Complexity
#         dp = [1] * n
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[j] += dp[j-1]
#         return dp[n-1]


if __name__ == "__main__":
    print(uniquePaths(30, 700))
