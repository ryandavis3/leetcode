import unittest
from dataclasses import dataclass
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


@dataclass(frozen=True)
class GameState:
    nums: List[int]
    turn: bool
    player_one_points: int
    player_two_points: int


def predict_winner(nums: List[int], turn: bool) -> int:
    print(nums)
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
    first_value = nums[0]
    last_value = nums[-1]
    if turn:
        choose_first_result = first_value + predict_winner(nums=nums[1:], turn=False)
        choose_last_result = last_value + predict_winner(nums=nums[:-1], turn=False)
    else:
        choose_first_result = -first_value + predict_winner(nums=nums[1:], turn=True)
        choose_last_result = -last_value + predict_winner(nums=nums[:-1], turn=True)
    return max(choose_first_result, choose_last_result)



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

    def test3(self) -> None:
        nums = [1, 5, 2]
        nums1 = predict_winner(nums=nums, turn=True)
        self.assertEqual(nums1, -2)

    def test4(self) -> None:
        nums = [1, 5, 233, 7]
        nums2 = predict_winner(nums=nums, turn=True)
        self.assertEqual(nums2, -2)