"""
Given a string "abc", print all the possible combinations.
Note that in combinations, ordering is immaterial ie. ab = ba. a ab ac abc b bc c

Input Format

abc

Constraints

All characters in the string are unique.

Output Format

a ab abc ac b bc c
"""


def printSubsequence(input, output):

    # Base Case
    # if the input is empty print the output string
    if len(input) == 0:
        print(output, end=" ")
        return

    # output is passed with including the
    # 1st character of input string
    printSubsequence(input[1:], output + input[0])

    # output is passed without including the
    # 1st character of input string
    printSubsequence(input[1:], output)


if __name__ == "__main__":
    output = ""
    input = "abc"

    printSubsequence(input, output)
