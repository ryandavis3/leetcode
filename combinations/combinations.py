from typing import List

# https://leetcode.com/problems/combinations/

def combine(n: int, k: int, md: int) -> List[List[int]]:
    """
    Given two integers n and k, return all possible combinations
    of k numbers out of 1...n.
    """
    # No digits left to add - finished!
    if k == 0:
        return [[]]
    # Recursively add digits to combination
    combs = []
    for ld in range(md, n+1): # Min digit to n
        rds = combine(n, k-1, ld+1)
        for rd in rds:
            combs += [[ld] + rd]
    return combs

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combine(n, k)
