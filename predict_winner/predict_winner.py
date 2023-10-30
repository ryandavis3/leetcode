import unittest
from typing import Dict, List, Tuple, Optional


class MemoizedMaxPoints:
    def __init__(self):
        self.max_points: Dict = {}

    def get(self, nums: List[int], turn: bool) -> Optional[int]:
        key = (tuple(nums), turn)
        if key in self.max_points:
            return self.max_points[key]
        return None

    def put(self, nums: List[int], turn: bool, points: int) -> None:
        key = (tuple(nums), turn)
        self.max_points[key] = points


def predict_winner(nums: List[int], turn: bool) -> int:
    if len(nums) == 1:
        value = nums[0]
        if turn:
            return value
        return -value
    if len(nums) == 2:
        difference = abs(nums[0] - nums[1])
        if turn:
            return difference
        return -difference



class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        pass


class TestPredictWinner(unittest.TestCase):
    def test1(self) -> None:
        nums = [5, 2]
        nums1 = predict_winner(nums=nums, turn=True)
        self.assertEqual(nums1, 3)
        nums2 = predict_winner(nums=nums, turn=False)
        self.assertEqual(nums2, -3)

    def test2(self) -> None:
        nums = [4]
        nums1 = predict_winner(nums=nums, turn=True)
        self.assertEqual(nums1, 4)
        nums2 = predict_winner(nums=nums, turn=False)
        self.assertEqual(nums2, -4)
