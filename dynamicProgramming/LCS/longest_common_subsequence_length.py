"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence
which is common in both the strings.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
 elements.

Example 1:
Input: s1 = "abdca"
       s2 = "cbda"
Output: 3
Explanation: The longest common subsequence is "bda".

Example 2:
Input: s1 = "passport"
       s2 = "ppsspt"
Output: 5
Explanation: The longest common subsequence is "psspt".

"""


def length_of_longest_common_subsequence_recursive(s1, s2, s1_len, s2_len):
    if s1_len == 0 or s2_len == 0:
        return 0

    if s1[s1_len - 1] == s2[s2_len - 1]:
        return 1 + length_of_longest_common_subsequence_recursive(
            s1, s2, s1_len - 1, s2_len - 1
        )
    else:
        return max(
            length_of_longest_common_subsequence_recursive(s1, s2, s1_len - 1, s2_len),
            length_of_longest_common_subsequence_recursive(s1, s2, s1_len, s2_len - 1),
        )


def length_of_longest_common_subsequence_memoize(s1, s2, s1_len, s2_len, dp):
    if s1_len == 0 or s2_len == 0:
        return 0

    if dp[s1_len][s2_len] != -1:
        return dp[s1_len][s2_len]

    if s1[s1_len - 1] == s2[s2_len - 1]:
        dp[s1_len][s2_len] = 1 + length_of_longest_common_subsequence_memoize(
            s1, s2, s1_len - 1, s2_len - 1, dp
        )
        return dp[s1_len][s2_len]
    else:
        dp[s1_len][s2_len] = max(
            length_of_longest_common_subsequence_memoize(
                s1, s2, s1_len, s2_len - 1, dp
            ),
            length_of_longest_common_subsequence_memoize(
                s1, s2, s1_len - 1, s2_len, dp
            ),
        )
        return dp[s1_len][s2_len]


def length_of_longest_common_subsequence_top_down(s1, s2):
    dp = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    # initialization
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
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            max_length = max(max_length, dp[i][j])
    return max_length


if __name__ == "__main__":
    s1 = "abdca"
    s2 = "cbda"
    print(length_of_longest_common_subsequence_recursive(s1, s2, len(s1), len(s2)))

    dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    print(length_of_longest_common_subsequence_memoize(s1, s2, len(s1), len(s2), dp))

    print(length_of_longest_common_subsequence_top_down(s1, s2))
