"""
https://leetcode.com/problems/insert-interval/
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
from typing import List

class Solution:
    def merge_interval(self, intervals: List[List[int]]) -> List[List[int]]:
        # if it was not sorted sort it.
        # intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        The array is already sorted so,
        1. Merge intervals in given intervals
        2. Add new_interval in correct location and merge interval
        (3,4)(7,8)  ---> add (4,8) --> (3,4), (4,8), (7,8) ---> merge interval
        """
        merged_intervals = intervals
        initial_size = len(merged_intervals)

        for i in range(len(intervals) - 1):
            if intervals[i][0] <= newInterval[0] < intervals[i + 1][0]:
                merged_intervals.insert(i + 1, newInterval)
            elif intervals[i][0] >= newInterval[0]:
                merged_intervals.insert(i, newInterval)

        if len(merged_intervals) == 1 and intervals[-1][0] > newInterval[0]:
            merged_intervals.insert(0, newInterval)
        if initial_size == len(merged_intervals):
            merged_intervals.append(newInterval)

        return self.merge_interval(merged_intervals)