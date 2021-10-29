# /*
#  *
#  * There are n buildings in New York City and as a real estate agent you decided to visit some of the buildings every day as follows:
# * 1 Visit one building.
# * 2 If the number of remaining buildings (n) is divisible by 2 then you can visit  n/2 buildings.
# * 3 If the number of remaining buildings (n) is divisible by 3 then you can visit  2*(n/3) buildings.
# You can only choose one of the strategies per day.
# Return the minimum number of days to visit n buildings.


# visited:   5, 1, 2, 1, 1
# remaining: 5, 4, 2, 1, 0
# 5 days


# visted:     1, 6, 2, 1
# remaining:  9, 3, 1, 0
# 4 days
# */

# n = 10

# visited:           5 1 2 1 1
# remaining:         5 4 2 1 0

#      0 1 2 3 4 5 6 7 8 9 10
# 1
# n//2
# n//3
look_up = {}


def minimum_number_of_days(n, loop_up):
    if n <= 0:
        return 0

    dp = [0] * n

    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1 + dp[n // 2] + dp[2 * n // 3]
    # min_two = loop_up.get(n//2,  minimum_number_of_days(n//2, loop_up))
    # look_up[n//2] = min_two
    #
    # min_three = look_up.get(2* n//3,  minimum_number_of_days(2 * n//3, loop_up))
    # look_up[2*n//3] = min_three

    return dp[n - 1]  # 1 + min(n-1, min_two, min_three)


if __name__ == "__main__":
    print(minimum_number_of_days(10, look_up))
