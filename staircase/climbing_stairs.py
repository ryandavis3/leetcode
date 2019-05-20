# https://leetcode.com/problems/climbing-stairs/

def climbStairs(N: int) -> int:
    """
    Get the number of distinct ways to climb to the
    top of a staircase with N steps. 
    
    The solution for N steps is equal to the N+1-th 
    Fibonacci number. 

    Compute in O(N) time. 
    """
    # Cases with 1 or 2 steps
    if N == 1:
        return 1
    elif N == 2:
        return 2
    # Cases with >2 steps
    n_2 = 1
    n_1 = 2
    i = 3
    while i <= N:
        n = n_1 + n_2
        n_2 = n_1
        n_1 = n
        i += 1  
    return n

class Solution:
    def climbStairs(self, n: int) -> int:
        return climbStairs(n)
