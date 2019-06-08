from typing import List

# https://leetcode.com/problems/spiral-matrix/

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    Given a matrix of m x n elements (m m, n columns), return 
    all elements of the matrix in spiral order.
    """
    # No matrix given
    if not matrix:
        return []
    # Get size of matrix, set initial direction and indices
    m = len(matrix)
    n = len(matrix[0])
    N = m * n
    direction = 'R'
    i = 0
    j = 0
    spiral = []
    # Set max index to traverse in each direction. Update
    # these during the algorithms so we make smaller 
    # linear traversals through the larger spiral traversal.
    R = n - 1
    D = m - 1
    L = 0
    U = 1
    # Traverse a spiral path until we have enough elements in the
    # new list. Our sequence of directions is right -> down -> left
    # -> up -> right. 
    while len(spiral) < N:
        # Add element to list
        spiral += [matrix[i][j]]
        # Go right
        if direction == 'R':
            if j < R:
                j += 1
            else:
                direction = 'D'
                i += 1
                R -= 1
        # Go down
        elif direction == 'D':
            if i < D:
                i += 1
            else:
                direction = 'L'
                j -= 1
                D -= 1
        # Go left
        elif direction == 'L':
            if j > L:
                j -= 1
            else:
                direction = 'U'
                i -= 1
                L += 1
        # Go up
        elif direction == 'U':
            if i > U:
                i -= 1
            else:
                direction = 'R'
                j += 1 
                U += 1
    return spiral

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return spiralOrder(matrix)
