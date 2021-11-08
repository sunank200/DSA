"""
You are given an array of events where events[i] = [startDayi, endDayi, valuei]
. The ith event starts at startDayi and ends at endDayi, and if you attend this
 event, you will receive a value of valuei. You are also given an integer k
 which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you
 must attend the entire event. Note that the end day is inclusive: that is,
 you cannot attend two events where one of them starts and the other ends on
 the same day.

Return the maximum sum of values that you can receive by attending events.

Example 1:
Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a
total value of 4 + 3 = 7.

https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
"""


from functools import lru_cache


def maxValue(events, k):
    # The number of events
    n = len(events)
    # Sort the events in chronological order
    events.sort()

    # k is the number of events we can attend
    # end is the last event we attended's END TIME
    # event_index is the current event we are checking
    @lru_cache(None)
    def dp(end: int, event_index: int, k: int):

        # No more events left or we have checked all possible events
        if k == 0 or event_index == n:
            return 0

        event = events[event_index]
        event_start, event_end, event_value = event
        # Can we attend this event?
        # Does its start time conflict with the previous events end time?
        # If the start time is the same as the end time we cannot end as well
        # (view example 2)
        if event_start <= end:
            # Could not attend, check the next event
            return dp(end, event_index + 1, k)

        # We made it here, so we can attend!
        # Two possible options, we either attend (add the value) or do not
        # attend this event
        # Value for attending versus the value for skipping
        attend = event_value + dp(event_end, event_index + 1, k - 1)
        skip = dp(end, event_index + 1, k)

        # Get the best option
        return max(attend, skip)

    # Clear cache to save memory
    dp.cache_clear()
    return dp(0, 0, k)


if __name__ == "__main__":
    print(maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2))
