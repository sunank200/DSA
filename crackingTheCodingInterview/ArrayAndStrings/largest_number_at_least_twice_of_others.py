"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much
as every other number in the array. If it is, return the index of the largest
element, or return -1 otherwise.



Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
Example 3:

Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number
because there are no other numbers.
"""


def dominantIndex(nums):
    """
    1. Iterate through the array and find largest, l_index
    2. Iterate the array again and find if largest > 2*nums[i], if not
    return -1
    3. if yes return l_index
    [1,2,3,4]
    [3,6,1,0]
    """
    if len(nums) == 1:
        return 0
    largest = -1
    l_index = -1
    for index, i in enumerate(nums):
        if i > largest:
            largest = i
            l_index = index
    print(largest, l_index)
    for i in range(len(nums)):
        if i == l_index:
            pass
        elif (2 * nums[i]) > largest:
            print(nums[i], i)
            return -1
    return l_index


if __name__ == "__main__":
    print(dominantIndex([3, 6, 1, 0]))
