"""https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it can trap after
 raining. Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6 Explanation: The above
elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,
2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""


def total_rain_water(height):
    # idea is to sum all water above each element.
    # compute max_left array
    # compute max_right array
    # water[i] = min(max_left[i], max_right[i]) - height[i]
    height_size = len(height)
    if height_size == 0:
        return 0

    max_left = [0] * height_size
    max_right = [0] * height_size

    max_left[0] = height[0]
    for i in range(1, height_size):
        max_left[i] = max(max_left[i - 1], height[i])

    max_right[height_size - 1] = height[-1]
    for i in range(height_size - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i])

    total_water = 0
    for i in range(0, height_size):
        total_water += min(max_right[i], max_left[i]) - height[i]

    return total_water


def test_total_rain_water():
    a_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert total_rain_water(a_1) == 6, "Test case:1 failed."

    a_2 = [4, 2, 0, 3, 2, 5]
    assert total_rain_water(a_2) == 9, "Test case: 2 failed."


if __name__ == "__main__":
    test_total_rain_water()
