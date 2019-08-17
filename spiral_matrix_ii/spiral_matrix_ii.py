from typing import List

# https://leetcode.com/problems/spiral-matrix-ii/

# Subsequent direction
D = {'R':'D', 'D':'L', 'L':'U', 'U':'R'}

def generateMatrix(n: int) -> List[List[int]]:
    """
    Given a positive integer n, generate a square matrix
    filled with elements from 1 to n**2 in spiral order.
    """
    # Empty matrix
    M = []
    for _ in range(n):
        M += [[None] * n]
    # Start in right direction; iterate until n**2 
    # values filled
    direction = 'R'
    i = 0
    j = 0
    k = 1
    while k <= n**2:
        # Add value to matrix
        M[i][j] = k
        # Right
        if direction == 'R':
            # Edge
            if j == n-1:
                direction = D[direction]
                i += 1
            # Filled value
            elif M[i][j+1] is not None:
                direction = D[direction]
                i += 1
            # Continue direction
            else:
                j += 1
        # Down
        elif direction == 'D':
            # Edge 
            if i == n-1:
                direction = D[direction]
                j -= 1
            # Filled value
            elif M[i+1][j] is not None:
                direction = D[direction]
                j -= 1
            # Continue diretion
            else:
                i += 1
        # Left
        elif direction == 'L':
            # Edge
            if j == 0:
                direction = D[direction]
                i -= 1
            # Filled value
            elif M[i][j-1] is not None:
                direction = D[direction]
                i -= 1
            # Continue diretion
            else:
                j -= 1
        # Up
        elif direction == 'U':
            # Edge
            if i == 0:
                direction = D[direction]
                j += 1
            # Filled value
            elif M[i-1][j] is not None:
                direction = D[direction]
                j += 1
            # Continue diretion
            else:
                i -= 1
        # Increment k 
        k += 1
    # Return filled matrix
    return M

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return generateMatrix(n)
