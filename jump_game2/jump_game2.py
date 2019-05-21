from typing import List

MAX = 10**5

def jump(nums: List[int]) -> List[int]:
    """
    Get minimum number of jumps to get to each 
    index in array.
    """
    L = len(nums)
    # Set initial values for jumps to large number
    min_jumps = [MAX]*L
    min_jumps[0] = 0
    prev_max_jump_L = 0
    # Iterate through each max jump length
    for i, max_jump_L in enumerate(nums):
        # If current max jump is less than the previous,
        # we do not need to search, since we can attain
        # all possible states with the previous in as many or
        # fewer jumps as the previous.
        if max_jump_L >= prev_max_jump_L:
            # Iterate over possible jumps from i 
            for j in range(1, max_jump_L+1):
                new_index = min(i + j, L-1)
                # Recurrence relation: check if new number of jumps
                # beats previous number of jumps.
                min_jumps[new_index] = min(min_jumps[new_index], min_jumps[i]+1)
        prev_max_jump_L = max_jump_L
    return min_jumps[-1]

class Solution:
    def jump(self, nums: List[int]) -> int:
        return jump(nums)
