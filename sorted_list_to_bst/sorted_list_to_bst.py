import math
from typing import List

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# First convert linked list to array, then re-use solution from 
# conversion of sorted array to BST.

class ListNode:
    """
    Node in a singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    """
    Node in binary search tree.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def listToArray(head: ListNode) -> List[int]:
    """
    Convert linked list to array.
    """
    arr = []
    while head:
        arr += [head.val]
        head = head.next
    return arr

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

def sortedListToBST(head: ListNode) -> TreeNode:
    """
    Convert sorted list to binary search tree.
    """
    nums = listToArray(head)
    return sortedArrayToBST(nums)

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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return sortedListToBST(head)
