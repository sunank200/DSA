"""
Given an array of meeting time intervals intervals where intervals[i] =
[starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""
import heapq


def minimum_meeting_room(intervals):
    """
    1. Sort the intervals based on start time
    2. add the end time of the interval to the min-heap, if it is empty or
    the start time of current interval to be added is less than end time on
    top of min heap, else pop from heap and add end time to heap.
    3. return the size of min-heap
    """

    intervals.sort(key=lambda x: x[0])

    min_heap = []
    for interval in intervals:
        if not min_heap or min_heap[0] > interval[0]:
            heapq.heappush(min_heap, interval[1])
        else:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])

    return len(min_heap)


if __name__ == "__main__":
    print(minimum_meeting_room([[0, 30], [5, 10], [15, 20]]))
