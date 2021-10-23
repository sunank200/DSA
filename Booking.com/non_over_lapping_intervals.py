"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest
of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""


def eraseOverlapIntervals(intervals):
    """
    Greedy approach based on starting points
     if two intervals are overlapping, we want to remove the interval that has the longer end point -- the longer interval will always overlap with more or the same number of future intervals compared to the shorter one
    1. sort intervals based on starting points
    2. prev = 0
    3. start from 1 to len(intervals)
        a. check if intervals[prev][1] > intervals[i][0]
                if intervals[prev][1] > intervals[i][1]
                    prev = i
                count++
        b. else:
                prev = i

    """

    if len(intervals) == 0:
        return 0

    intervals.sort(key=lambda x: x[0])

    prev = 0
    count = 0

    for i in range(1, len(intervals)):
        if intervals[prev][1] > intervals[i][0]:
            if intervals[prev][1] > intervals[i][1]:
                prev = i
            count += 1
        else:
            prev = i
    return count


if __name__ == "__main__":
    print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(eraseOverlapIntervals([[1, 2], [2, 3]]))
    print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
