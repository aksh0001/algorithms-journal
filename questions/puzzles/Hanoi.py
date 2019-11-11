"""
Towers of Hanoi Problem.
We have three rods and n discs.
The objective of the puzzle is to move the entire stack of discs to another rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
    i.e. a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.

REF: https://www.youtube.com/watch?v=8lhxIOAfDss

@author a.k
"""
SOURCE, AUX, DEST = "A", "B", "C"


def move(from_rod, to_rod):
    """
    Moves a disc from the from_rod to the to_rod
    :param from_rod: source rod
    :param to_rod: destination rod
    :return: none
    """
    print('Move disc from {} to {}'.format(from_rod, to_rod))


def solve(n: int, from_rod, aux_rod, to_rod):
    """
    Moves n discs from the source rod (from_rod) to the destination rod (to_rod) using the auxiliary rod (aux_rod).
    :param n: total number of discs
    :param from_rod: source rod
    :param aux_rod: auxiliary rod
    :param to_rod: destination rod
    :Time: O(2^n)
    :return: none
    """
    if n == 0:  # BC: If no discs, nothing to move
        return
    # Step 1: Recursively move n-1 discs from source rod to aux rod via destination rod
    solve(n - 1, from_rod, to_rod, aux_rod)
    # Step 2: Using the last disc on the source rod, move it to the destination rod
    move(from_rod, to_rod)
    # Step 3: Recursively move the n-1 discs (now sitting on aux) to destination rod via source rod
    solve(n - 1, aux_rod, from_rod, to_rod)


def detailed_solve(n, from_rod, aux_rod, to_rod):
    if n == 0:
        return
    detailed_solve(n - 1, from_rod, to_rod, aux_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    detailed_solve(n - 1, aux_rod, from_rod, to_rod)


if __name__ == '__main__':
    solve(3, SOURCE, AUX, DEST)
    # print('DETAILS:')
    # detailed_solve(3, SOURCE, AUX, DEST)
