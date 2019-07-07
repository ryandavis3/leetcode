from typing import List, Dict

# https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums: List[int]) -> int:
    """
    Given an unsorted array of integers, find the length of the
    longest consecutive element sequence in O(n) time.
    """
    # Edge cases - array has zero or one element
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    # Maintain two dictionaries with keys as starting (ending) values
    # of consecutive subsequences and values as lengths of subsequences.
    start = {}
    end = {}
    for num in nums:
        add = True
        if num in start or num in end:
            continue
        # Add to front of subsequence
        if num + 1 in start:
            s = num
            e = s + start[num+1] 
            L = start[num+1] + 1
            start[s] = L
            del start[num+1]
            end[e] = L
            add = False
        # Add to back of subsequence
        if num - 1 in end:
            s = num - end[num-1]
            e = num - 1
            L = end[num-1] 
            # Combine subsequences if possible
            if num in start:
                e = e + start[num]
                L = L + start[num]
                del start[num]
            else:
                e = e + 1
                L = L + 1
            start[s] = L
            end[e] = L
            del end[num-1]
            add = False
        # Number cannot be added to existing subsequence - create new one.
        if add:
            start[num] = 1
            end[num] = 1
    return max(start.values())

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return longestConsecutive(nums)
