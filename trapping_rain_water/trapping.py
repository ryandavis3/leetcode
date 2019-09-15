from typing import List

# https://leetcode.com/problems/trapping-rain-water/

def trap(height: List[int]) -> int:
    """
    Given n non-negative integers representing an elevation
    map where the width of each bar is 1, compute how much
    water it is able to trap after raining.
    """
    # No heights passed!
    if not height:
        return 0
    # Max from left
    max_L = 0
    L = len(height)
    left = [0] * L
    for i in range(L):
        if height[i] > max_L:
            max_L = height[i]
        left[i] = max_L
    # Max from right
    max_R = 0
    right = [0] * L
    for i in range(L-1, -1, -1):
        if height[i] > max_R:
            max_R = height[i]
        right[i] = max_R
    # Get water height / area at each point on map
    area = 0
    for i in range(1, L-1):
        area += max(0, min(left[i-1], right[i+1]) - height[i])
    return area

class Solution:
    def trap(self, height: List[int]) -> int:
        return trap(height)
