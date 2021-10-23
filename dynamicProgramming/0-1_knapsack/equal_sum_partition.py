"""
Given a non-empty array nums containing only positive integers, find if
the array can be partitioned into two subsets such that the sum of elements
in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


def subset_sum(arr, sum):
    dp = [[False for _ in range(sum + 1)] for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        dp[i][0] = True

    for j in range(1, sum + 1):
        dp[0][j] = False

    for i in range(1, len(arr) + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(arr)][sum]


def equal_sum_partition(arr):
    arr_sum = sum(arr)

    if arr_sum % 2 != 0:
        return False
    else:
        return subset_sum(arr, arr_sum // 2)


def test():
    t1 = [1, 2, 3, 5]
    assert equal_sum_partition(t1) is False, "Test case 1 failed."

    t2 = [1, 5, 11, 5]
    assert equal_sum_partition(t2) is True, "Test case 2 failed."


if __name__ == "__main__":
    test()
