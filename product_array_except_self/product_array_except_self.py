from typing import List

# https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Given an array of n integers where n>1, return an array 
    output such that output[i] is equal to the product of all elements 
    of nums except nums[i].
    
    Build lists of cumulative products to the left and right 
    of the number.
    """
    L = len(nums)
    # Product to the left of element
    left = [None] * L
    left[0] = nums[0]
    for i in range(1, L):
        left[i] = left[i-1] * nums[i]
    # Product to the right of element
    right = [None] * L
    right[L-1] = nums[L-1]
    for j in range(L-2, -1, -1):
        right[j] = right[j+1] * nums[j]
    # Multiply left and right products to get full product
    # excluding the element.
    output = [None] * L
    for k in range(L):
        if not k:
            output[k] = right[1]
        elif k == L-1:
            output[k] = left[L-2]
        else:
            output[k] = left[k-1] * right[k+1]
    return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return productExceptSelf(nums)
