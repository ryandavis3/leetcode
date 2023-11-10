from unittest import TestCase
from typing import List


def get_max_score(nums: List[int], k: int) -> int:
    i = k
    j = k
    L = len(nums)
    min_value = nums[k]
    max_score = min_value
    while i > 0 or j < L - 1:
        min_value = min(min_value, nums[i], nums[j])
        score = min_value * (j - i + 1)
        if score > max_score:
            max_score = score
        if i == 0:
            j += 1
        elif j == L - 1:
            i -= 1
        elif nums[i-1] < nums[j+1]:
            j += 1
        else:
            i -= 1
    return max_score


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        pass


class TestMaxScore(TestCase):
    def test1(self) -> None:
        max_score = get_max_score(nums=[1, 4, 3, 7, 4, 5], k=3)
        self.assertEqual(max_score, 15)

    def test2(self) -> None:
        max_score = get_max_score(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0)
        self.assertEqual(max_score, 20)

    def test3(self) -> None:
        max_score = get_max_score(nums=[1, 2, 7, 8, 7, 1], k=2)
        self.assertEqual(max_score, 21)

    def test4(self) -> None:
        nums = [4, 5, 4, 1, 1, 7, 5, 5]
        max_score = get_max_score(nums=nums, k=2)
        self.assertEqual(max_score, 12)

    def test5(self) -> None:
        nums = [4, 5, 4, 1, 1, 7, 5, 5]
        max_score = get_max_score(nums=nums, k=5)
        self.assertEqual(max_score, 15)