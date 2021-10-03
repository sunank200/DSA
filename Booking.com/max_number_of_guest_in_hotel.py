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

Output : 2


"""


def question_implementation(input):
    days = {}
    for i in input:
        for k in range(i[0], i[1] + 1):
            if k in days:
                days[k] += 1
            else:
                days[k] = 1

    return sorted(days.items(), key=lambda x: x[1], reverse=True)[0][0]


import heapq


def high_days(guests):
    """
    The problem stated does not look like a real one. In real world if one
    person leaves on day 5 and to persons arrive on day 5, there are only 2
     guests in the hotel on that day. Because visitors usually leave before
     new visitors arrive.
    According to this amendment my solution would be
    :param guests:
    :return:
    """
    schedule = []

    for arrive, depart in guests:
        heapq.heappush(schedule, (arrive, 1))
        heapq.heappush(schedule, (depart, -1))

    current_guests = max_day = max_day_guests = 0

    while schedule:
        day, inout = heapq.heappop(schedule)
        current_guests += inout
        if current_guests > max_day_guests:
            max_day = day
            max_day_guests = current_guests

    return max_day, max_day_guests


if __name__ == "__main__":
    guests = [
        (1, 4),
        (2, 5),
        (10, 12),
        (5, 9),
        (5, 12),
    ]
    print(high_days(guests))

    input = [(1, 4), (2, 5), (10, 12), (5, 9), (5, 12)]
    print(question_implementation(input))
