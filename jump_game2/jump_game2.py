from typing import List

MAX = 10**5

def jumps(nums: List[int]) -> List[int]:

    L = len(nums)
    min_jumps = [MAX]*L
    min_jumps[0] = 0
    for i, max_jump_len in enumerate(nums):
        for j in range(1, max_jump_len+1):
            new_index = min(i + j, L-1)
            min_jumps[new_index] = min(min_jumps[new_index], min_jumps[i]+1)
    return min_jumps

class Solution:
    def jump(self, nums: List[int]) -> int:
        return jumps(nums)[-1]
