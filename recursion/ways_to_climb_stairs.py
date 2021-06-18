"""
Given a staircase of n steps and a set of possible steps that we can climb at
a time named possibleSteps, create a function that returns the number of ways
a person can reach to the top of staircase.

Example:
    Input:
        n = 10
        possibleSteps = [2,4,5,8]
    Output: 11

    Explanation:
        [2,2,2,2,2], [2,2,2,4], [2,2,4,2], [2,4,2,2], [4,2,2,2], [4,4,2],
    [2,4,4], [4,2,4], [5,5], [8,2], [2,8]

    idea here is lets say if someone is at step 2, number of ways one can
    jump to step 10 is (10-2)->8 ways and similarly


    ways(10) = ways(10-2) + ways(10-4) + ways(10-5) + ways(10-8)
    i.e:
    ways(10) = ways(8) + ways(6) + ways(5) + ways(2)

    ways to jump to 10-2
                [2,2,2,2], [4,4] ,[2,2,4], [8], [2,4,2], [4,2,2]
"""


def wtj(stair, possible_steps, call_stack) -> int:
    call_stack.append(stair)
    print(call_stack)
    if stair == 0:  # only one way to jumping to step 0
        call_stack.pop()
        print(call_stack)
        return 1
    no_of_ways = 0

    for steps in possible_steps:
        if stair - steps >= 0:
            no_of_ways += wtj(stair - steps, possible_steps, call_stack)
    call_stack.pop()
    print(call_stack)
    return no_of_ways


if __name__ == "__main__":
    stairs = 10
    possible_steps = [2, 4, 5, 8]
    print(wtj(10, possible_steps, []))
