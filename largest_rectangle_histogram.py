from unittest import TestCase
from typing import Dict, List, Optional


class Rectangles:
    def __init__(self, height_width: Optional[Dict[int, int]]=None, max_area: int=0):
        if height_width is None:
            self._height_width: Dict[int, int] = {}
        else:
            self._height_width = height_width
        self.max_area = max_area

    def process_bar(self, bar: int):
        height_width_new: Dict[int, int] = {}
        height_width_new[bar] = 1
        if bar > self.max_area:
            self.max_area = bar
        for height, width in self._height_width.items():
            if bar >= height:
                height_width_new[height] = width + 1
                area = height * (width + 1)
                if area > self.max_area:
                    self.max_area = area
            else:
                if width + 1 > height_width_new[bar]:
                    height_width_new[bar] = width + 1
                    area = bar * (width + 1)
                    if area > self.max_area:
                        self.max_area = area
        return Rectangles(height_width=height_width_new, max_area=self.max_area)


def get_largest_rectangle_area(heights: List[int]) -> int:
    rectangles = Rectangles()
    for bar in heights:
        rectangles = rectangles.process_bar(bar=bar)
    return rectangles.max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return get_largest_rectangle_area(heights=heights)


class TestRectangles(TestCase):

    def test1(self) -> None:
        rectangles = Rectangles()
        heights = [2, 3]
        for bar in heights:
            rectangles = rectangles.process_bar(bar=bar)
        self.assertEqual(rectangles._height_width, {2: 2, 3: 1})
        self.assertEqual(rectangles.max_area, 4)

    def test2(self) -> None:
        heights = [2, 1, 5, 6, 2, 3]
        largest_area = get_largest_rectangle_area(heights=heights)
        self.assertEqual(largest_area, 10)

    def test3(self) -> None:
        rectangles = Rectangles()
        heights = [2, 1, 2]
        for bar in heights:
            rectangles = rectangles.process_bar(bar=bar)
        self.assertEqual(rectangles._height_width, {2: 1, 1: 3})
        self.assertEqual(rectangles.max_area, 3)

    def test4(self) -> None:
        rectangles = Rectangles()
        heights = list(range(1, 10))
        for bar in heights:
            rectangles = rectangles.process_bar(bar=bar)
            print(rectangles._height_width)
        assert False

