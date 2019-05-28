import copy
from typing import List

# https://leetcode.com/problems/combination-sum/

def addElementToLists(lists: List[List[int]], val: int) -> List[List[int]]:
    """
    Add element to every list in a group of lists.
    """
    lists = copy.deepcopy(lists)
    for l in lists:
        l += [val]
    return lists

def combinationSum(candidates: List[int], target: int):
    """
    Given a set of numbers (candidates) and a target number 
    (target), find all unique combinations where the numbers 
    sum to the target. 

    Use dynamic programming.
    """
    # Store combinations for intermediate values in dictionary
    D = dict()
    # Iterate over intermediate values to target
    for num in range(1, target+1):
        D[num] = []
        if num in candidates:
            D[num] += [[num]]
        # Subtract each candidate and build on solutions 
        # for previous intermediate values.
        for cand in candidates:
            diff = num - cand
            if diff <= 0:
                continue
            if not D[diff]:
                continue
            D[num] += addElementToLists(D[diff], cand)
    if not D[target]:
        return []
    # Get unique combinations for target
    combs = [tuple(sorted(comb)) for comb in D[target]]
    combs = list(set(combs))
    combs = [list(comb) for comb in combs]
    return combs        

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return combinationSum(candidates, target)
