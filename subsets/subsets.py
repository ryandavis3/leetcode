from typing import List, FrozenSet

# https://leetcode.com/problems/subsets/

class Subset:
    """
    Class for subset of integers. 
    """
    def __init__(self, used: FrozenSet, free: FrozenSet):
        """
        Constructor. 

        Args:
            used (frozenset): Integers in subset.
            free (frozenset): Integers in larger set not in subset.
        """
        self.used = used
        self.free = free
    def __eq__(self, other):
        return self.used == other.used
    def __hash__(self):
        return hash(self.used)
    def to_list(self):
        return list(self.used)

def findSubsets(nums: List[int]) -> List[List[int]]:
    """
    Find the power set (all possible subsets) of a list
    of distinct integers.
    
    Use dynamic programming. Build length N+1 subsets
    by adding an unused letter to each length N subset.
    """
    # Degenerate case
    if not nums:
        return [[]]
    # n = 0 case -> empty string
    N = len(nums)
    # Use frozenset rather than set to allow hashing
    nums = frozenset(nums)
    subsets_prev = [Subset(used=frozenset(), free=nums)]
    subsets_all = [[]]
    # Recursively build larger sets while numbers left to add
    n = 1
    while n <= N:
        subsets_n = []
        # Try adding letters to each subset of length n-1
        for subset_i in subsets_prev:
            free = set(subset_i.free)
            used = set(subset_i.used)
            for i, char in enumerate(free):
                used_i = used.copy()
                used_i.add(char)
                free_i = free.copy()
                free_i.remove(char)
                subsets_n += [Subset(frozenset(used_i), frozenset(free_i))]
        # Remove duplicate subsets of length n
        subsets_n = list(set(subsets_n))
        # Represent subsets as list of int
        subsets_all += [s.to_list() for s in subsets_n]   
        subsets_prev = subsets_n
        n += 1
    return subsets_all

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return findSubsets(nums)
