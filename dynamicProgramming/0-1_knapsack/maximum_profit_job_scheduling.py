"""
We have n jobs, where every job is scheduled to be done from startTime[i] to
endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum
profit you can take such that there are no two jobs in the subset with
overlapping time range.

If you choose a job that ends at time X you will be able to start another
job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""


def find_max_profit(jobs, n, position, dp):
    if position == n:
        return 0

    if position in dp:
        return dp[position]

    _, end, current_profit = jobs[position]

    for j in range(position + 1, len(jobs)):
        if end <= jobs[j][0]:
            current_profit += find_max_profit(jobs, n, j, dp)
            break

    profit_without_current_index = find_max_profit(jobs, n, position + 1, dp)
    max_profit = max(profit_without_current_index, current_profit)

    dp[position] = max_profit
    return max_profit


def jobSchedulingMemoize(startTime, endTime, profit):
    """
        For this problem, the key is to understand for any given ith job,
        we can make choice

    1. pick up ith job, our profit will be profit[i] + profit of the job we can
     finish before i-th job
    2. do not pick up the ith job, we keep the previous max profit

    First we need to combine all the inputs (not sure why there are 3 - does
    not make sense to me);
    Then we can sort the jobs by its end time, it will help us to find the
    first job can be done before we pick up the ith job;
    Lastly we start making choices by the rule stated above:
    """
    if len(startTime) != len(endTime) != len(profit):
        return 0

    jobs = []

    for i in range(len(profit)):
        jobs.append([startTime[i], endTime[i], profit[i]])

    jobs = sorted(jobs, key=lambda x: x[0])

    dp = {}

    return find_max_profit(jobs, len(profit), 0, dp)


def jobSchedulingbuttomup(startTime, endTime, profit):
    jobs = list(zip(startTime, endTime, profit))

    # sort by end time
    jobs.sort(key=lambda x: (x[1]))

    n = len(jobs)

    dp = [0] * (n)
    prev = [-1] * (n)

    # calculate the first job can be picked up before ith job
    for i in range(1, n):
        for j in reversed(range(i)):
            if jobs[j][1] <= jobs[i][0]:
                prev[i] = j
                break

    # init
    dp[0] = jobs[0][2]
    for i in range(1, n):
        # if there is no job to be picked up, we can only continue to have the
        # previous Max or pick the ith job
        if prev[i] == "-1":
            dp[i] = max(dp[i - 1], jobs[i][2])
        else:
            # we can pick i-th job, plus the previous Max
            # or we do not pick up the i-th job
            dp[i] = max(jobs[i][2] + dp[prev[i]], dp[i - 1])
    return dp[-1]


if __name__ == "__main__":
    print(jobSchedulingMemoize([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
    print(jobSchedulingbuttomup([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
