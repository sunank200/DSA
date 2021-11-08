"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens
puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
"""

class Solution:
    def backtrack(self, row, diagonal, anti_diagonal, cols, n):
        # Base case - N queens have been placed
        if row == n:
            return 1

        solution = 0
        for col in range(n):
            curr_diagonal = row - col
            curr_anti_diagonal = row + col

            # If the queen is not placeable
            if col in cols or curr_diagonal in diagonal or curr_anti_diagonal in anti_diagonal:
                continue

            # "Add" the queen to the board
            cols.add(col)
            diagonal.add(curr_diagonal)
            anti_diagonal.add(curr_anti_diagonal)

            # Move on to the next row with the updated board state
            solution += self.backtrack(row + 1, diagonal, anti_diagonal, cols, n)

            # "Remove" the queen from the board since we have already
            # explored all valid paths using the above function call
            cols.remove(col)
            diagonal.remove(curr_diagonal)
            anti_diagonal.remove(curr_anti_diagonal)

        return solution

    def totalNQueens(self, n: int) -> int:
        """
        1.If the current row we are considering is greater than n, then we have a solution. Return 1.

        2. Initiate a local variable solutions = 0 that represents all the possible solutions that can be obtained from the current board state.

        3. Iterate through the columns of the current row. At each column, we will attempt to place a queen at the square (row, col) - remember we are considering the current row through the function arguments.

            a. Calculate the diagonal and anti-diagonal that the square belongs to. If there has been no queen placed yet in the column, diagonal, or anti-diagonal, then we can place a queen in this column, in the current row.
            b. If we can't place the queen, skip this column (move on to try with the next column).
        4. If we were able to place a queen, then update our 3 sets (cols, diagonals, and antiDiagonals), and call the function again, but with row + 1.

        5. The function call made in step 4 explores all valid board states with the queen we placed in step 3. Since we're done exploring that path, backtrack by removing the queen from the square - this just means removing the values we added to our sets.
        """
        return self.backtrack(0, set(),set(), set(), n)