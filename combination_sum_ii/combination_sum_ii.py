import copy
from typing import List, Dict
from collections import Counter

# https://leetcode.com/problems/combination-sum-ii/

def lowerCount(count: Dict, val: int) -> None:
    """
    Lower the count of value by one.
    """
    count[val] -= 1
    if count[val] == 0:
        del count[val]

def removeDuplicates(ls: List) -> List:
    """
    Remove duplicates in list of lists.
    """
    ls = [tuple(sorted(l)) for l in ls]
    ls = list(set(ls))
    ls = [list(l) for l in ls]
    return ls

def combinationSum(candidates: Dict, target: int) -> List[List[int]]:
    """
    Given a collection of candidate numbers (candidates) and a 
    target number (target), find all unique combinations in candidates
    where the candidate numbers sum to target. Each nunmber in 
    candidates may only be used once in the combination.
    """
    # No candidates left!
    if not candidates:
        return None
    # All candidates too large!
    if min(candidates) > target:
        return None
    # Found candidate matching target!
    combs = []
    if target in candidates:
        combs += [[target]]
    # Try each candidate
    for c in candidates:
        if c < target:
            cn = copy.deepcopy(candidates)
            lowerCount(cn, c)
            tn = target - c
            # Recursively find combinations for smaller target
            combsum = combinationSum(cn, tn)
            if combsum is not None:
                combsums = [[c] + cs for cs in combsum]
                combs += combsums
    # No working combinations!
    if not combs:
        return None
    # Remove duplicates
    combs = removeDuplicates(combs)
    return combs

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = Counter(candidates)
        return combinationSum(candidates, target)
