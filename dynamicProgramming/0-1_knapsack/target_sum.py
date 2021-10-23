"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+'
and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates
to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be
target 3.

-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""


def count_subset_sum(nums, target_sum, zero_count):
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(nums) + 1)]

    for i in range(len(nums) + 1):
        dp[i][0] = 1

    for j in range(1, target_sum + 1):
        dp[0][j] = 0

    for i in range(1, len(nums) + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(nums)][target_sum] * pow(2, zero_count)


def findTargetSumWays(nums, target):
    """
    This is equivalent to count of two subset whose diff is equal to target.
    1. This is equivalent to count of two subset whose diff is equal to sum.
    2. s1 + s2 = range
    3. s1 - s2 = target
    4. s1 = (range + target) // 2
    5. top down subset_sum
    6. make a matrix of size n+1 by (range + target) // 2 + 1
    7. first row is zero
    8 first col is 1
    9. if nums[i-1] <= (range + target) // 2
            dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
    10. Edge cases: target > range , return 0
                    if range == 0, return pow(2,len(nums))
                    count zeros and remove from num
                    ans = dp[len(nums)][target_sum] * pow(2,zero_count)
    """
    ranges = sum(nums)

    if target > ranges or (target + ranges) % 2 != 0 or target < -ranges:
        return 0

    if ranges == 0:
        return pow(2, len(nums))

    target_sum = (target + ranges) // 2

    zero_count = 0
    for i in nums:
        if i == 0:
            zero_count += 1

    for _ in range(zero_count):
        nums.remove(0)

    return count_subset_sum(nums, target_sum, zero_count)


if __name__ == "__main__":
    print(findTargetSumWays([1, 1, 1, 1, 1], 3))
