"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which
 is common in both the strings.

Example 1:
Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".

Example 2:
Input: s1 = "passport"
       s2 = "ppsspt"
Output: 3
Explanation: The longest common substring is "ssp".
"""


def find_LCS_length(s1, s2):
    n1, n2 = len(s1), len(s2)
    maxLength = min(n1, n2)
    dp = [[[-1 for _ in range(maxLength)] for _ in range(n2)] for _ in range(n1)]
    return find_LCS_length_recursive(dp, s1, s2, 0, 0, 0)


def find_LCS_length_recursive(dp, s1, s2, i1, i2, count):
    if i1 == len(s1) or i2 == len(s2):
        return count

    if dp[i1][i2][count] == -1:
        c1 = count
        if s1[i1] == s2[i2]:
            c1 = find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2 + 1, count + 1)
        c2 = find_LCS_length_recursive(dp, s1, s2, i1, i2 + 1, 0)
        c3 = find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2, 0)
        dp[i1][i2][count] = max(c1, max(c2, c3))

    return dp[i1][i2][count]


def longest_common_substring_length(s1, s2):
    dp = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    max_length = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 0
            max_length = max(max_length, dp[i][j])

    return max_length


if __name__ == "__main__":
    s1 = "abdca"
    s2 = "cbda"
    print(longest_common_substring_length(s1, s2))

    print(find_LCS_length(s1, s2))
