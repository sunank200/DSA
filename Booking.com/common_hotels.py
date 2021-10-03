"""
Given arrays for N (>= 2) users, each representing the IDs of hotels visited,
find the common IDs of the hotels visited amongst the users.

Input:
userA = { 2, 3, 1 }
userB = { 2, 5, 3 }
userC = { 7, 3, 1 }

Output:
{3}

Assumptions:
Arrays are unsorted.

Cases:
1) Each array consists of distinct hotel IDs
2) Each array may contain duplicate hotel IDs
"""


def intersection_of_hotels(user_hotel_visits):
    visit_occurance = {}
    result = set()
    for each_user_visit in user_hotel_visits:
        for hotel_id in each_user_visit:
            visit_occurance[hotel_id] = visit_occurance.get(hotel_id, 0) + 1
            if visit_occurance.get(hotel_id) == len(user_hotel_visits):
                result.add(hotel_id)
    return result


if __name__ == "__main__":
    A = [2, 3, 1]
    B = [2, 5, 3]
    C = [7, 3, 1]
    user_visits = [set(A), set(B), set(C)]
    print(intersection_of_hotels(user_visits))
