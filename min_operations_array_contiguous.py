from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pass


def get_min_operations(nums: List[int]) -> int:
    nums = sorted(nums)
    max_subseq_len = 1
    curr_subseq_len = 1
    L = len(nums)
    for i in range(1, L):
        if nums[i] == nums[i+1] - 1:
            curr_subseq_len += 1
            if curr_subseq_len > max_subseq_len:
                max_subseq_len = curr_subseq_len
        else:
            curr_subseq_len = 1
    return L - curr_subseq_len