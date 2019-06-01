from typing import List

# https://leetcode.com/problems/3sum-closest/

def sign(num: int):
    if num >= 0:
        return 1
    else:
        return -1

def twoSumClosest(L: List[int], target: int) -> int:

    # Set indices at start and end of list
    i = 0
    j = len(L)-1
    # First iteration
    sum_ij = L[i] + L[j]
    diff = target - sum_ij
    if len(L) == 2:
        return diff
    min_diff = 10**10
    result = [i, j, 0, sum_ij]
    if diff > 0:
        i += 1
    elif diff < 0:
        j -= 1
    # Iterate through list
    result = None
    while i < j and j:
        # Difference between current sum and target
        sum_ij = L[i] + L[j]
        diff = target - sum_ij
        # Exact match! 
        if diff == 0:
            min_diff = 0
            #result = [i, j, 0, sum_ij]
            break
        # If sign of difference changes, either the current
        # sum or the previous sum is the closest.
        if abs(diff) < abs(min_diff):
            #result = [i, j, 0, sum_ij]
            min_diff = diff
        # Need larger sum - remove first element
        if diff > 0:
            i += 1
        # Need smaller sum - remove last element
        elif diff < 0:
            j -= 1
    #if not result:
        #result = [i, j, diff, sum_ij]
    return min_diff

def threeSumClosest(nums: List[int], target: int) -> int:

    nums = sorted(nums)
    closest_diff = 10**10
    closest_index = [-1, -1, -1]
    for i, num in enumerate(nums):
        L = nums.copy()
        L.remove(num)
        t = target - num
        diff = twoSumClosest(L, t)
        if diff == 0:
            return target
        #print('Diff: %s' % diff)
        if abs(diff) < abs(closest_diff):
            closest_sum = target - diff
            #print('Sum: %s' % closest_sum)
            closest_diff = diff
    return closest_sum

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return threeSumClosest(nums, target)
