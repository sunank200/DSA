"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square
 containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
"""


def maximalSquare(matrix):
    """
    1. initialize another matrix (dp) with the same dimensions as the original one initialized with all 0’s.
    2. dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.
    3.dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.
    4. maintain the size of maximum square till now

    """

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    max_length = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                max_length = max(max_length, dp[i][j])

    return max_length * max_length


if __name__ == "__main__":
    print(
        maximalSquare(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
    )
