from unittest import TestCase
from typing import List


def get_increasing_triplet(nums: List[int]) -> bool:
    n = len(nums)
    dp = [1] * n
    min_element = 0
    for i in range(n):
        if nums[i] <= min_element:
            min_element = nums[i]
            continue
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
                if dp[i] >= 3:
                    return True
    return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        return get_increasing_triplet(nums=nums)


class TestIncreasingTriplet(TestCase):
    def test1(self) -> None:
        nums = [1, 2, 3, 4, 5]
        self.assertTrue(get_increasing_triplet(nums=nums))

    def test2(self) -> None:
        nums = [5, 4, 3, 2, 1]
        self.assertFalse(get_increasing_triplet(nums=nums))

    def test3(self) -> None:
        nums = [2, 1, 5, 0, 4, 6]
        self.assertTrue(get_increasing_triplet(nums=nums))

    def test4(self) -> None:
        nums = [20, 100, 10, 12, 5, 13]
        self.assertTrue(get_increasing_triplet(nums=nums))

    def test5(self) -> None:
        nums = [1] * 10 ** 3 + [2, 3]
        result = get_increasing_triplet(nums=nums)
        self.assertTrue(result)