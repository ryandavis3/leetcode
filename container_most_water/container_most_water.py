from typing import List

# https://leetcode.com/problems/container-with-most-water/

def maxArea(height: List[int]) -> int:
    """
    Brute force solution -> O(n^2) -> too slow.
    """
    # Iterate over each pair of integers
    area = 0
    for i, h1 in enumerate(height):
        for j, h2 in enumerate(height):
            a = abs(i-j) * min(h1, h2)
            if a > area:
                area = a
    return area

def maxArea2(height: List[int]) -> int:
    """
    Solution with two pointers.
    """
    L = len(height)
    left = 0
    right = L - 1
    max_area = 0
    move = 'L'
    while left < right:
        
        area = (right - left) * min(height[left], height[right])
        if area > max_area:
            max_area = area

        if left == 0 and right == L - 1: 
            max_l = height[left]
            max_r = height[right]
        
        if move == 'L':
            while height[left] <= max_l and left < right:
                left += 1
            max_l = height[left]
            move = 'R'
        elif move == 'R':
            while height[right] <= max_l and left < right:
                right -= 1
            max_r = height[right]
            move = 'L'
   
    return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return maxArea2(height)
