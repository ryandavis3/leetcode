from unittest import TestCase
from typing import List


SENTINEL = -1


def get_largest_rectangle_area(heights: List[int]) -> int:
    stack = [SENTINEL]
    max_area = 0
    L = len(heights)
    for i in range(L):
        while stack[-1] != SENTINEL and heights[stack[-1]] >= heights[i]:
            current_height = heights[stack.pop()]
            current_width = i - stack[-1] - 1
            current_area = current_height * current_width
            max_area = max(current_area, max_area)
        stack.append(i)

    while stack[-1] != SENTINEL:
        current_height = heights[stack.pop()]
        current_width = L - stack[-1] - 1
        current_area = current_height * current_width
        max_area = max(current_area, max_area)

    return max_area




class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return get_largest_rectangle_area(heights=heights)


class TestLargestRectangleArea(TestCase):
    def test1(self) -> None:
        heights = [2, 3]
        largest_area = get_largest_rectangle_area(heights=heights)
        self.assertEqual(largest_area, 4)

    def test2(self) -> None:
        heights = [5, 6, 7, 10, 3, 8, 1]
        largest_area = get_largest_rectangle_area(heights=heights)
        self.assertEqual(largest_area, 20)

