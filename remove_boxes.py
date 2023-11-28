from dataclasses import dataclass
from unittest import TestCase
from typing import List


@dataclass(frozen=True)
class BoxRow:
    number: int
    length: int


class Boxes:
    def __init__(self, boxes: List[int]):
        self._boxes = boxes
        self._box_locations: Dict[int, BoxRow] = {}
        start = 0
        prev = boxes[0]
        L = len(boxes)
        for i, box in enumerate(boxes):
            if i == 0:
                continue
            if box != prev:
                print('a')
                box_row = BoxRow(number=prev, length=i-start)
                self._box_locations[start] = box_row
                start = i
                prev = box
        if start < L -1:
            box_row = BoxRow(number=prev, length=L-1-start)
            self._box_locations[start] = box_row


def remove_boxes(boxes: List[int]) -> int:
    pass


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        pass


class TestBoxes(TestCase):
    def test1(self) -> None:
        boxes = [1, 1, 1, 2, 2]
        boxes_ = Boxes(boxes=boxes)
        expected_box_locations = {0: BoxRow(number=1, length=3), 3: BoxRow(number=2, length=1)}
        self.assertEqual(boxes_._box_locations, expected_box_locations)


class TestRemoveBoxes(TestCase):
    def test1(self) -> None:
        boxes = [1, 1, 1]
        output = remove_boxes(boxes=boxes)
        self.assertEqual(output, 9)

    def test2(self) -> None:
        boxes = [1]
        output = remove_boxes(boxes=boxes)
        self.assertEqual(output, 1)