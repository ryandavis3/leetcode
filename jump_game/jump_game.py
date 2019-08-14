from typing import List

# https://leetcode.com/problems/jump-game/

def canJump(nums: List[int]) -> bool:
    """
    Return True if we can "jump" to the last index,
    else return False.

    We are initially positioned at the first index of 
    the array. Each element in the array represents
    the max jump length at that position.
    """
    # Start at end of array; need value of at least one
    # to reach.
    need = 1
    # Iterate from end to beginning of array
    L = len(nums)
    for i in range(L-2, -1, -1):
        # Able to reach index i -> reset needed value to 1
        if nums[i] >= need:
            need = 1
        # Not enough to reach end -> increment needed value
        else:
            need += 1
    # Return True if we are able to reach end from first index
    return need <= 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return canJump(nums)
