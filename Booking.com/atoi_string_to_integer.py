"""
mplement the myAtoi(string s) function, which converts a string to a 32-bit
signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-'
or '+'. Read this character in if it is either. This determines if the final
 result is negative or positive respectively. Assume the result is positive if
 neither is present.
Read in next the characters until the next non-digit charcter or the end of the
 input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no
digits were read, then the integer is 0. Change the sign as necessary (from
step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then
clamp the integer so that it remains in the range. Specifically, integers less
 than -231 should be clamped to -231, and integers greater than 231 - 1 should
  be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of
 the string after the digits.
"""


def myAtoi(s):
    """
    Algorithm:

    First Strip to remove the whitespaces ahead.
    Make sure you are checking for + and - sign both at the first index.
    split the string and look at only the first element of the list formed.
    Follow the algorithm given in the description.
    Time: O(N)
    Space: O(k) - k is the length of digit in string.
    """
    s = s.strip()
    if not s:
        return 0

    sign = 1
    num = ""
    s_lst = s.split()
    # for packet in s_lst:
    if s_lst[0][0] in "1234567890":
        num = s_lst[0]
    elif s_lst[0][0] in ["-", "+"]:
        num = s_lst[0][1:]
        if s_lst[0][0] == "-":
            sign = -1

    out = 0
    for idx in range(len(num)):
        if num[idx].isdigit():
            out = out * 10 + ord(num[idx]) - ord("0")
        else:
            break

    out = out * sign

    if out > (2 ** 31 - 1):
        return 2 ** 31 - 1
    elif out < -1 * (2 ** 31):
        return -1 * (2 ** 31)
    else:
        return out


if __name__ == "__main__":
    print(myAtoi("-42"))
