from dataclasses import dataclass
from typing import List


@dataclass
class Monster:
    distance: int
    speed: int
    time_to_city: int


def step_minute_forward(monster: Monster) -> Monster:
    distance = self.distance - speed
    time_to_city = self.time_to_city - 1
    return Monster(distance=distance, speed=monster.speed, time_to_city=time_to_city)


def eliminate_max(dist: List[int], speed: List[int]) -> int:
    pass


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        pass