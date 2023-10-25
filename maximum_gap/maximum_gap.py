from typing import List


def maximum_gap(nums: List[int]) -> int:
    max_gap = 0
    nums = sorted(nums)
    for i in range(len(nums)):
        if i == 0:
            continue
        max_gap_i = nums[i] - nums[i-1]
        if max_gap_i > max_gap:
            max_gap = max_gap_i
    return max_gap


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        return maximum_gap(nums=nums)