from typing import List

# https://leetcode.com/problems/n-queens

def solve(n: int, i: int, a: List[int], b: List[int], c: List[int]):
    """
    Use a generator function with recursion to solve the N-Queens
    problem.
    
    Args:
        a (list of int): Positions of queens. a[i] = val means
            there is a queen in column i and row val.
        b (list of int): Sum of row, col for lower left diagonal.
        c (list of int): Sum of row, col for upper left diagonal.
    """
    # Incomplete board; add a queen in column i
    if i < n:
        # Try to place a queen in each row (within column)
        for j in range(n):
            # Check horizontal, diagonal attacking queens
            if j not in a and i+j not in b and i-j not in c:
                for solution in solve(n, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    # Complete board
    else:
        yield a

def translate(L: List[int], N: int) -> List[str]:
    """
    Translate solution from more concise queen position format 
    to more verbose string format.

    Example:
        [1, 3, 0, 2] -> ['..Q.', 'Q...', '...Q', '.Q..']
    """
    Ls = []
    for col, row in enumerate(L):
        s = col * '.' + 'Q' + (N-col-1) * '.'
        Ls += [[row, s]]
    Ls = sorted(Ls, key=lambda x: x[0])
    Ls = [x[1] for x in Ls]
    return Ls

def solveNQ(N: int) -> List[int]:
    """
    Solve N-Queens problem.
    """
    # Get all solutions using generator approach.
    sols = []
    for sol in solve(N, 0, [], [], []):
        sols += [sol]
    # Translate solutions into '.Q' string format
    sols = [translate(sol, N) for sol in sols]
    return sols

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return solveNQ(n)
