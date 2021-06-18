"""
Tower of Hanoi is a mathematical puzzle where we have
3 rods and n disks. The objective of the puzzle is to
move the entire stack to another rod, obeying the
following simple rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk
from one of the Stack and placing it on top of another
stack i.e. a disk can only be moved if it is the
uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.

The goal is to move all the disks from the leftmost
rod to the rightmost rod

Write a program which prints a sequence of operations
that move n disks from one rod to another.
Also, you need to find the total moves.

Example 1:

Input:
N = 2
Output:
move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
3
Explanation: For N=2 , steps will be
as follows in the example and total
3 steps will be taken.

Approach:
a - 1,2,3    b    c

base condtion -> if pole has 1 dis move from a to c

move n-1 disc from a to b
move n-1 disc from b to c

total move = 2^(n-1)
"""


class Towerofhanoi:
    def __init__(self):
        self.moves = 0

    def solve(self, n, source, destination, aux):
        """
        Prints the moves to shift disc from source to destination.
        :param n: number of disc
        :param source: source pole
        :param destination: destination pole
        :param aux: auxillary pole or helper pole
        :return: returns number of moves
        """

        if n == 1:
            print(f"Move disk {n} from rod {source} to rod {destination}.")
            self.moves += 1
            return self.moves

        self.solve(n - 1, source, aux, destination)
        print(f"Move disk {n} from rod {source} to rod {destination}.")
        self.solve(n - 1, aux, destination, source)
        return self.moves


if __name__ == "__main__":
    toh = Towerofhanoi()
    moves = toh.solve(10, "A", "C", "B")
    print("Total moves: {}".format(moves))
