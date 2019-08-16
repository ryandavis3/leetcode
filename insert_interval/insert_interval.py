from typing import List

# https://leetcode.com/problems/insert-interval/

## Current solution runs in O(n) time. Can we make it run
## in O(log n) time using binary search? I think so!!

def insert(intervals: List[List[int]], newInterval: List[int]):
    """
    Given a set of non-overlapping intervals, insert a new interval
    into the intervals (merge if necessary)
    """
    # No intervals given!
    if not intervals:
        return [newInterval]
    # Initialize key values
    L = len(intervals)
    [start, end] = newInterval
    i = 0
    combine = False
    remove = []
    non_overlap = None
    # Iterate until we reach end of list of intervals
    while i < L:
        # New interval overlaps with at least some of existing interval
        if start >= intervals[i][0] and start <= intervals[i][1] and end >= intervals[i][1]: 
            intervals[i][1] = end 
            start = min(intervals[i][0], start) # Remember start of overlapped interval
            combine = True
        # New interval overlaps with all of existing interval
        elif start <= intervals[i][0] and end >= intervals[i][0]:
            intervals[i][0] = start
            intervals[i][1] = max(intervals[i][1], end)
            # Check if we are in combine mode -> if yes, add overlapped interval to remove list
            if combine:
                remove += [intervals[i-1]] 
            combine = True
        # New interval at beginning of list
        elif i == 0 and end < intervals[i][0]:
            non_overlap = 0
        # New interval at end of list
        elif i == L-1 and intervals[i][1] < start:
            non_overlap = L
        # New interval between two existing intervals
        elif start > intervals[i][1] and end < intervals[i+1][0]:
            non_overlap = i + 1
        i += 1
    # Remove intervals
    for interval in remove:
        intervals.remove(interval)
    # Add new interval to list
    if non_overlap is not None:
        intervals = intervals[:non_overlap] + [newInterval] + intervals[non_overlap:] 
    return intervals


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return insert(intervals, newInterval)
