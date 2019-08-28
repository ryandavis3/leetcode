from typing import List

# https://leetcode.com/problems/container-with-most-water/

def maxArea(height: List[int]) -> int:
    """
    Given n noon-negative integers a1, a2, ..., an, where each
    represents a point a coordinate (i, ai). n vertical lines are 
    drawn such that the two endpoints of line i are at (i, ai) and
    (i, 0). Find two lines which together the the x-axis forms
    a container such that the container contains the most water.
    """
    # Use two pointers, one at left (right) end of array
    L = len(height)
    left = 0
    right = L - 1
    max_area = 0
    # Start with widest possible container and search containers
    # with smaller widths (and larger heights)
    while left < right:
        # Compute area for pair; update max area
        area = (right - left) * min(height[left], height[right])
        if area > max_area:
            max_area = area
        # Set initial max left (right) heights
        if left == 0 and right == L - 1: 
            max_l = height[left]
            max_r = height[right]
        # Move left pointer to the right
        if height[left] < height[right]:
            while height[left] <= max_l and left < right:
                left += 1
            max_l = height[left]
        # Move right pointer to the left
        else:
            while height[right] <= max_r and left < right:
                right -= 1
            max_r = height[right]
    # Return max area
    return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return maxArea(height)
