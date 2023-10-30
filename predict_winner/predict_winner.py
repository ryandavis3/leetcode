from typing import Dict, List, Tuple


class MemoizedMaxPoints:
    def __init__(self):
        self.max_points: Dict = {}

    def get(self, nums_sum: List[int], turn: bool) -> Optional[int]:
        key = (tuple(nums_sum), turn)
        if key in self.max_points:
            return self.max_points[key]
        return None

    def put(self, nums_sum: List[int], turn: bool, points: int) -> None:
        key = (tuple(nums_sum), turn)
        self.max_points[key] = points


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        pass