import math
from typing import List

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class TreeNode:
    """
    Node in binary search tree.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def midLeftRight(nums: List[int]) -> List:
    """
    Return midpoint, left subarray, and right subarray
    of sorted array.
    """
    L = len(nums)
    i = math.floor(L/2)
    mid = nums[i]
    left = nums[:i]
    right = nums[i+1:]
    return [mid, left, right]

def sortedArrayToBST(nums: List[int]) -> TreeNode:
    """
    Convert sorted array to binary search tree.
    """
    if not nums:
        return None
    [mid, left, right] = midLeftRight(nums)
    root = TreeNode(mid)
    root.left = sortedArrayToBST(left)
    root.right = sortedArrayToBST(right)
    return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return sortedArrayToBST(nums) 
