from typing import List, Dict

# https://leetcode.com/problems/4sum/

def getTwoSumDict(nums: List[int]) -> Dict:
    """
    Make dictionary representing possible sums of any
    two distinct elements in a list.
    """
    D = {}
    L = len(nums)
    # Iterate through list
    for i in range(L):
        for j in range(i+1, L):
            _sum = nums[i] + nums[j]
            if _sum not in D:
                D[_sum] = []
            # Add indices of elements summing to value
            D[_sum] += [set([i, j])]
    return D

def combineTwoSumSets(L1: List[set], L2: List[set]):
    """
    Combine sets of elements only where both sets
    are completely non-overlapping.
    """
    comb = []
    for s1 in L1:
        for s2 in L2:
            if not s1 & s2: # No common elements
                comb += [tuple(s1.union(s2))]
    return comb

def getFourSum(nums: List[int], target: int):
    """
    Get all unique quadruplets giving a sum of a target value.
    
    Use a divide and conquer approach by first finding
    couples summing to target values and then combining 
    couples.
    """
    # Get dictionary of elements summing to two
    D = getTwoSumDict(nums)
    # Find combinations of couples adding to target
    comb = []
    for key in D:
        target_small = target - key
        if target_small in D:
            L1 = D[key]
            L2 = D[target_small]
            comb += combineTwoSumSets(L1, L2)
    # Get values from indices and get unique combinations
    comb = list(set(comb))
    comb_vals = []
    for index in comb:
        comb_vals += [tuple(sorted([nums[i] for i in index]))]
    comb_vals = list(set(comb_vals))
    comb_vals = [list(cv) for cv in comb_vals]
    return comb_vals

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return getFourSum(nums, target)
