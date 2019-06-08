from typing import List

# https://leetcode.com/problems/merge-intervals/

def mergeIntervals(L: List[List[int]]) -> List[List[int]]:
    """
    Make one pass through a list of intervals, merging one 
    with the next if overlapping.
    """
    # Start and end values of intervals
    starts = [x[0] for x in L]
    ends = [x[1] for x in L]
    # Initial values for merged list and index
    N = len(L)
    M = []
    i = 0
    n_merge = 0
    # Iterate through list
    while i < N-1:
        # Merge one interval with the next
        if ends[i] >= starts[i+1]:
            M += [[starts[i], max(ends[i], ends[i+1])]]
            i += 2
            n_merge += 1
        # Do not merge; add interval as-is
        else:
            M += [[starts[i], ends[i]]]
            i += 1
    # Add last interval if missed
    if i < N:
        M += [[starts[i], ends[i]]]
    return [M, n_merge]


def merge(L: List[List[int]]) -> List[List[int]]:
    """
    Given a collection of intervals, merge all overlapping
    intervals.
    """
    # Sort on start of index
    L = sorted(L, key=lambda x: x[0])
    # Recursively merge intervals in list until no more
    # merges are possible.
    n_merge = 1
    while n_merge > 0:
        [L, n_merge] = mergeIntervals(L)
    return L 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return merge(intervals)
