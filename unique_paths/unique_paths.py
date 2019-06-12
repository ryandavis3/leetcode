from math import factorial

# https://leetcode.com/problems/unique-paths/

def uniquePaths(m: int, n: int) -> int:
    """
    A robot is in the top left corner of an m x n grid. The robot 
    can move down or right at any point in time. Compute the number 
    of unique paths to the bottom right corner of the grid. 

    Need to make m-1 right (R) moves and n-1 down (D) moves. Reduce problem
    to number of permutations of a string with m-1 R's and n-1 D's.

    (m+n-2)! / ((n-1)!(m-1)!)
    """
    return int(factorial(m+n-2) / (factorial(m-1) * factorial(n-1)))

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return uniquePaths(m, n)
