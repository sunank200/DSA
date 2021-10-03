"""
You are given two lists of closed intervals, firstList and secondList,
where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x
 with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are
either empty or represented as a closed interval. For example, the intersection
 of [1, 3] and [2, 4] is [2, 3].
"""


def intervalIntersection(firstList, secondList):
    """
    1. As intervals are sorted and disjoint.
    2. take end of 1 and end of start of 2, is end1 < start2, merged
    add[end2,start1] or start2
    """

    intersections = []

    i = j = 0

    while i < len(firstList) and j < len(secondList):
        # Let's check if A[i] intersects B[j].
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection

        lo = max(firstList[i][0], secondList[j][0])
        hi = min(firstList[i][1], secondList[j][1])

        if lo <= hi:
            intersections.append([lo, hi])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1
    return intersections


if __name__ == "__main__":
    print(
        intervalIntersection(
            [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
        )
    )
