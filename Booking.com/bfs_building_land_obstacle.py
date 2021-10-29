"""
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the
shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to
build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the
 friends and the meeting point.

The distance is calculated using Manhattan Distance, where
distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

"""
import collections
import itertools


def shortestDistance(grid) -> int:
    """
    1. Idea is to compute the shortest distance between each empty land and a
    building pair.
    2. To do that, we run BFS starting from each building and update the
    shortest distance to each land that we come across.
    3. Once BFS has finished running for all buildings, we simply compute the
    sum of the distances to all buildings for each land and select the minimum.
    4. If this minimum is less than Inf, we know such a land is a possibility
    and return the minimum we found, otherwise we return -1.


    """

    if not grid:
        return -1

    # create a list of buildings and a set of empty lands for easy search later
    build, land = [], set()

    for x, y in itertools.product(range(len(grid)), range(len(grid[0]))):
        if grid[x][y] == 0:
            land.add((x, y))
        elif grid[x][y] == 1:
            build.append((x, y))

    # if there is no empty land available, we can't proceed further
    if not land:
        return -1

    # create a dictionary where each land's position tuple is a key and its value is a list of length equal to the number of buildings we found above.
    # This list is populated with Inf, to start with, that will be updated by the
    # shortest distance between the land and building pair, found by BFS routine below.
    d = {x: [float("inf")] * len(build) for x in land}

    # BFS for a given building's location
    def BFS(loc):
        x, y = build[loc]
        # (x,y) is building's location on the grid and 0 is the starting distance
        q = collections.deque([(x, y, 0)])
        while q:
            x, y, dist = q.popleft()
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                # we are interested in only traversing lands whose recorded distance from
                # current building is more than dist+1. We update their distance and include
                # these lands in our queue for the next layer, if that's the case
                if (i, j) in land and d[(i, j)][loc] > dist + 1:
                    d[(i, j)][loc] = dist + 1
                    q.append((i, j, dist + 1))

    # run BFS routine for all buildings
    for loc in range(len(build)):
        BFS(loc)

    # compute the shortest distance to all buildings for each empty land
    min_dist = min(sum(d[x]) for x in land)
    return -1 if min_dist == float("inf") else min_dist


if __name__ == "__main__":
    print(shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
