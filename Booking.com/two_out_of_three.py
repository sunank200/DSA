"""
You have three Arrays.
A = {2, 5, 3, 2, 8,1}
B = {7, 9, 5, 2, 4, 10, 10}
C = {6, 7, 5, 5, 3, 7}

make an array from this three arrays which elements is present in at least two
array.

Return the sorted list of numbers that are present in at least 2 out of the 3
arrays.

This question was followed by instead of three arrays. If you have a list of
array then what will be the solution? Also what will be the time complexity?
"""
A = [2, 5, 3, 2, 8, 1]
B = [7, 9, 5, 2, 4, 10, 10]
C = [6, 7, 5, 5, 3, 7]

import heapq


def two_out_of_three(A, B, C):
    """
    sort all the lists.
    create a dict of occurance of all the element.
    use set of result and add value to set only if the element already exists
    in occurance dict
    :param A:
    :param B:
    :param C:
    :return:
    """
    A = set(A)
    B = set(B)
    C = set(C)
    list_of_lists = [A, B, C]
    occurance_dict = {}
    result = set()

    for list_curr in list_of_lists:
        for elm in list_curr:
            if elm in occurance_dict:
                result.add(elm)
            else:
                occurance_dict[elm] = occurance_dict.get(elm, 0) + 1

    return sorted(result)


if __name__ == "__main__":
    print(two_out_of_three(A, B, C))
