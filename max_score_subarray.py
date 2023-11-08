from unittest import TestCase
from typing import List


def get_score_update(min_element: int, i: int, j: int, max_score: int) -> int:
    score = min_element * (j - i + 1)
    if score > max_score:
        max_score = score
    return max_score


def get_max_score(nums: List[int], k: int) -> int:
    i = 0
    j = max(k, 1)
    L = len(nums)
    min_element = min(nums[i:j+1])
    max_score = min_element * (j - i + 1)
    while i <= k and j < L:
        if nums[i] == min_element and i < k:
            i += 1
            min_element = min(nums[i:j+1])
            max_score = get_score_update(min_element=min_element, i=i, j=j, max_score=max_score)
            continue
        while k <= j < L and nums[j] >= min_element:
            max_score = get_score_update(min_element=min_element, i=i, j=j, max_score=max_score)
            j += 1
        if j < L:
            min_element = nums[j]
    if j == L:
        j_sweep = L - 1
        while i <= k:
            min_element = min(nums[i:j_sweep + 1])
            max_score = get_score_update(min_element=min_element, i=i, j=j_sweep, max_score=max_score)
            i += 1
    return max_score


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        return get_max_score(nums=nums, k=k)


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


