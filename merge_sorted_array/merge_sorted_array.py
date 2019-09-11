from typing import List

# https://leetcode.com/problems/merge-sorted-array/

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge two sorted integer arrays.
    """
    # Set variables
    nums3 = [0]*(m+n)
    i = 0
    j = 0
    k = 0
    # Iterate while values left in either array
    while i < m or j < n: 
        # Check if we have completed one of the arrays
        if i >= m:
            nums3[k] = nums2[j]
            j += 1
        elif j >= n:
            nums3[k] = nums1[i]
            i += 1
        # Add smaller value to merged list
        elif nums1[i] <= nums2[j]:
            nums3[k] = nums1[i]
            i += 1
        else:
            nums3[k] = nums2[j]
            j += 1
        # Increment index of merged list
        k += 1
    for i, val in enumerate(nums3):
        nums1[i] = val


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merge(nums1, m, nums2, n)
