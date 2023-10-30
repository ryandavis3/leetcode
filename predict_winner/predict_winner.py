from typing import List
from collections import defaultdict


def predict_winner(nums: List[int]) -> bool:

    n = len(nums)
    def max_diff(left: int, right: int) -> int:
        if left == right:
            return nums[0]
        max_left = nums[left] - max_diff(left+1, right)
        max_right = nums[right] - max_diff(left, right-1)
        return max(max_left, max_right)

    return max_diff(0, n-1)


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        pass