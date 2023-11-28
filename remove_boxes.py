from unittest import TestCase
from typing import List


class Boxes:
    def __init__(self, boxes: List[int]):
        self._boxes = boxes
        self._box_locations: Dict[int, Set]



def remove_boxes(boxes: List[int]) -> int:
    pass


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        pass


class TestRemoveBoxes(TestCase):
    def test1(self) -> None:
        boxes = [1, 1, 1]
        output = remove_boxes(boxes=boxes)
        self.assertEqual(output, 9)

    def test2(self) -> None:
        boxes = [1]
        output = remove_boxes(boxes=boxes)
        self.assertEqual(output, 1)