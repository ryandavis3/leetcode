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


class MemoizedMaxPointsInstance:
    _instance: Optional[MemoizedMaxPoints] = None


def get_memoized_singleton() -> MemoizedMaxPoints:
    if MemoizedMaxPointsInstance._instance is None:
        memoized_max_points = MemoizedMaxPoints()
        MemoizedMaxPointsInstance._instance = memoized_max_points
    return MemoizedMaxPointsInstance._instance


@dataclass(frozen=True)
class GameState:
    nums: List[int]
    turn: bool
    player_one_points: int
    player_two_points: int


def predict_winner(game_state: GameState) -> int:
    memoized_max_points = get_memoized_singleton()
    max_points = memoized_max_points.get(nums=game_state.nums, turn=game_state.turn)
    if max_points is not None:
        return max_points
    next_turn = not game_state.turn
    if len(game_state.nums) == 1:
        if game_state.turn:
            player_one_points = game_state.player_one_points + game_state.nums[0]
            player_two_points = game_state.player_two_points
        else:
            player_one_points = game_state.player_one_points
            player_two_points = game_state.player_two_points + game_state.nums[0]
        max_points = player_one_points - player_two_points
        memoized_max_points.put(nums=game_state.nums, turn=game_state.turn, points=max_points)
        return max_points
    if len(game_state.nums) == 2:
        max_points = max(game_state.nums)
        min_points = min(game_state.nums)
        if game_state.turn:
            player_one_points = game_state.player_one_points + max_points
            player_two_points = game_state.player_two_points + min_points
        else:
            player_one_points = game_state.player_one_points + min_points
            player_two_points = game_state.player_two_points + max_points
        max_points = player_one_points - player_two_points
        memoized_max_points.put(nums=game_state.nums, turn=game_state.turn, points=max_points)
        return max_points
    first_value = game_state.nums[0]
    last_value = game_state.nums[-1]
    if game_state.turn:
        next_game_state_first = GameState(
            nums=game_state.nums[1:],
            turn=next_turn,
            player_one_points=game_state.player_one_points + first_value,
            player_two_points=game_state.player_two_points,
        )
        choose_first_result = predict_winner(game_state=next_game_state_first)
        next_game_state_last = GameState(
            nums=game_state.nums[:-1],
            turn=next_turn,
            player_one_points=game_state.player_one_points + last_value,
            player_two_points=game_state.player_two_points,
        )
        choose_last_result = predict_winner(game_state=next_game_state_last)
        max_points = max(choose_first_result, choose_last_result)
        memoized_max_points.put(nums=game_state.nums, turn=game_state.turn, points=max_points)
        return max_points
    else:
        next_game_state_first = GameState(
            nums=game_state.nums[1:],
            turn=next_turn,
            player_one_points=game_state.player_one_points,
            player_two_points=game_state.player_two_points + first_value,
        )
        choose_first_result = predict_winner(game_state=next_game_state_first)
        next_game_state_last = GameState(
            nums=game_state.nums[:-1],
            turn=next_turn,
            player_one_points=game_state.player_one_points,
            player_two_points=game_state.player_two_points + last_value,
        )
        choose_last_result = predict_winner(game_state=next_game_state_last)
        max_points = max(choose_first_result, choose_last_result)
        memoized_max_points.put(nums=game_state.nums, turn=game_state.turn, points=max_points)
        return max_points



class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        game_state = GameState(nums=nums, turn=True, player_one_points=0, player_two_points=0)
        points = predict_winner(game_state=game_state)
        if points < 0:
            return False
        return True


class TestPredictWinner(unittest.TestCase):
    def test1(self) -> None:
        print(MemoizedMaxPointsInstance._instance)
        game_state = GameState(
            nums=[5, 2],
            turn=True,
            player_one_points=0,
            player_two_points=0,
        )
        nums1 = predict_winner(game_state=game_state)
        self.assertEqual(nums1, 3)
        game_state = GameState(
            nums=[5, 2],
            turn=False,
            player_one_points=0,
            player_two_points=0,
        )
        nums2 = predict_winner(game_state=game_state)
        self.assertEqual(nums2, -3)

    def test2(self) -> None:
        game_state = GameState(
            nums=[4],
            turn=True,
            player_one_points=0,
            player_two_points=0,
        )
        nums1 = predict_winner(game_state=game_state)
        self.assertEqual(nums1, 4)
        game_state = GameState(
            nums=[4],
            turn=False,
            player_one_points=0,
            player_two_points=0,
        )
        nums2 = predict_winner(game_state=game_state)
        self.assertEqual(nums2, -4)

    def test3(self) -> None:
        game_state = GameState(
            nums=[1, 5, 2],
            turn=True,
            player_one_points=0,
            player_two_points=0,
        )
        nums1 = predict_winner(game_state=game_state)
        self.assertEqual(nums1, -2)

    def test4(self) -> None:
        game_state = GameState(
            nums=[1, 5, 233, 7],
            turn=True,
            player_one_points=0,
            player_two_points=0,
        )
        nums2 = predict_winner(game_state=game_state)
        self.assertEqual(nums2, 222)

    def test5(self) -> None:
        game_state = GameState(
            nums=[2, 4, 55, 6, 8],
            turn=True,
            player_one_points=0,
            player_two_points=0,
        )
        nums2 = predict_winner(game_state=game_state)
        self.assertEqual(nums2, 222)

