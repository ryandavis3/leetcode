from unittest import TestCase
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return find_pattern(nums=nums)


def find_pattern(nums: List[int]) -> bool:
    N = len(nums)
    # No possibility of pattern if N < 3
    if N < 3:
        return False
    # Compute min array
    min_array = [0] * N
    for i, num in enumerate(nums):
        if i == 0:
            min_array[i] = num
            continue
        min_array[i] = min(min_array[i-1], num)
    # Use stack to find 132 pattern
    stack = list()
    for j in range(N - 1, -1, -1):
        # Array element not greater than minimum
        if nums[j] <= min_array[j]:
            continue
        # Pop elements from stack until we find an element which
        # satisfies nums[k] > nums[i]
        while stack and stack[-1] <= min_array[j]:
            stack.pop()
        # Check if we have nums[k] < nums[j]
        if stack and stack[-1] < nums[j]:
            return True
        stack.append(nums[j])
    return False


class TestPattern(TestCase):
    def test1(self) -> None:
        nums = [1, 2, 3, 4]
        pattern = find_pattern(nums=nums)
        self.assertFalse(pattern)

    def test2(self) -> None:
        nums = [3, 1, 4, 2]
        pattern = find_pattern(nums=nums)
        self.assertTrue(pattern)

    def test3(self) -> None:
        nums = [-1, 3, 2, 0]
        pattern = find_pattern(nums=nums)
        self.assertTrue(pattern)

    def test4(self) -> None:
        nums = [5, 2, 4, 3]
        pattern = find_pattern(nums=nums)
        self.assertTrue(pattern)

    def test5(self) -> None:
        nums = [1, 2, 3, 2, 1]
        pattern = find_pattern(nums=nums)
        self.assertTrue(pattern)

    def test6(self) -> None:
        nums = [1, 0, 1, -4, -3]
        pattern = find_pattern(nums=nums)
        self.assertFalse(pattern)

    def test7(self) -> None:
        nums = [3, 2, 1, 2, 5]
        pattern = find_pattern(nums=nums)
        self.assertFalse(pattern)