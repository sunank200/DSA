"""
Problem Description

Given an integer array A containing N integers.

You need to divide the array A into two subsets S1 and S2 such that the
absolute difference between their sums is minimum.

Find and return this minimum possible absolute difference.

NOTE:

Subsets can contain elements from A in any order (not necessary to be
contiguous).
Each element of A should belong to any one subset S1 or S2, not both.
It may be possible that one subset remains empty.


Problem Constraints
1 <= N <= 100

1 <= A[i] <= 100



Input Format
First and only argument is an integer array A.



Output Format
Return an integer denoting the minimum possible difference among the sums of two subsets.



Example Input
Input 1:

 A = [1, 6, 11, 5]


Example Output
Output 1:

 1


Example Explanation
Explanation 1:

 Subset1 = {1, 5, 6}, sum of Subset1 = 12
 Subset2 = {11}, sum of Subset2 = 11

"""


def subset_sum(arr, target_sum):
    dp = [[False for _ in range(target_sum + 1)] for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        dp[i][0] = True

    for j in range(1, target_sum + 1):
        dp[0][j] = False

    for i in range(len(arr) + 1):
        for j in range(target_sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp


def solve(A):
    """
    Overall idea here is s1 - s2 = min_diff
    but s1 + s2 = range, s2 = range - s1

    so, 2*s1 - range = min_diff

    so it translates to count the number of subset with given sum...
    here target_sum = range
    last row in top down matrix, find min_diff
    """
    ranges = sum(A)

    dp = subset_sum(A, ranges)

    last_row = dp[-1]

    min_diff = float("inf")
    for i in range(len(last_row) // 2, -1, -1):
        if last_row[i] == True:
            min_diff = abs(ranges - 2 * i)
            break

    return min_diff


if __name__ == "__main__":
    print(solve([1, 6, 11, 5]))
