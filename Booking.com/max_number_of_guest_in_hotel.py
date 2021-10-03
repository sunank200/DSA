"""
Consider a hotel where the guest is checked in and check out. Find a day when
the maximum number of guests stay in a hotel.

example:

Input :
[
{check-in : 1, check-out 4},
{check-in : 2, check-out 5},
{check-in : 10, check-out 12},
{check-in : 5, check-out 9},
{check-in : 5, check-out 12}
]

Output : 5

https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/
"""


def maximum_interval_overlap(intervals):
    """
    1. sort both arrival and departure times
    2. if arrive2 <= exit1
    there an overlap if arrival time of next is less than departure time of previous one
    increase the guest_in and max_guest
    else decerment guest_in
    :param intervals:
    :return:
    """

    if len(intervals) == 0:
        return 0, 0
    arrive = [interval[0] for interval in intervals]
    depart = [interval[1] for interval in intervals]

    arrive.sort()
    depart.sort()

    guest_in = 1
    max_guest = 1

    days = arrive[0]

    i = 1
    j = 0

    while i < len(intervals) and j < len(intervals):
        if arrive[i] <= depart[j]:
            # there an overlap if arrival time of next is less than departure time of previous one
            guest_in += 1

            if guest_in > max_guest:
                max_guest = guest_in
                days = arrive[i]

            i += 1
        else:
            guest_in -= 1
            j += 1

    return max_guest, days


"""
Another Efficient Solution : 
Approach : 
1). Create an auxiliary array used for storing dynamic data of starting and 
ending points.
2). Loop through the whole array of elements and increase the value at the s
tarting point by 1 and similarly decrease the value after ending point by 1. 
[Here we use the expressions “x[start[i]]-=1” and “x[end[i]+1]-=1”]
3). While looping, after calculating the auxiliary array: permanently add the
 value at current index and check for the maximum valued index traversing from 
 left to right.
Time Complexity : O(max(departure time)) 
Auxiliary Space : O(max(departure time)) 
"""


if __name__ == "__main__":
    guest_timings = [(1, 4), (2, 5), (10, 12), (5, 9), (5, 12)]
    print(maximum_interval_overlap(guest_timings))
