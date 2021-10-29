"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
 diagram below).

Now consider if some obstacles are added to the grids. How many unique paths
 would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


def uniquePathsWithObstacles(obstacleGrid):
    """
    1. number of ways to go right in first row -> 1
    2. number of ways to go down in first cols -> 1
    3. if obstacle, we won't let that cell contribute to any path.
    4. use dp:
        1. use given grid so no extra space needed.
        2. if first cell->1, return 0
        3. Otherwise, if obstacleGrid[0,0] has a 0 originally we set it to 1 and move ahead.
        4. iterate first row, if cell has obstacle 1, set the value to 0. else. obstraclegrid[i][j] = obstaclegrid[i][j-1]
        5. iterate first col, if the cell has obstacle, set value to 0. else
        obstaclegrid[i][j] = obstaclegrid[i-1][j]
        6. Now iterate through array starting from obstaclegrid[1][1], if it doesn't have obstacle, one can reach there from up and left, so
        obstaclegrid[i][j] = obstaclegrid[i-1][j] + obstaclegrid[i][j-1]

        7. if the cell has obstacle set it to 0 and continue
    """
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])

    if not obstacleGrid or len(obstacleGrid) == 0:
        return 0

    # if first cell has obstacle, return 0
    if obstacleGrid[0][0] == 1:
        return 0

    # number of ways of reaching 0,0
    obstacleGrid[0][0] = 1

    # first cols
    for i in range(1, rows):
        obstacleGrid[i][0] = int(
            obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1
        )

    # first row
    for j in range(1, cols):
        obstacleGrid[0][j] = int(
            obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1
        )

    # fill rest of rows and cols
    for i in range(1, rows):
        for j in range(1, cols):
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
            else:
                obstacleGrid[i][j] = 0
    return obstacleGrid[rows - 1][cols - 1]


if __name__ == "__main__":
    print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
