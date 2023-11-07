from unittest import TestCase
from dataclasses import dataclass
from typing import List


@dataclass
class Monster:
    distance: int
    speed: int
    time_to_city: int

    @classmethod
    def from_distance_speed(cls, distance: int, speed: int):
        time_to_city = (distance + 0.0) / speed
        return cls(distance=distance, speed=speed, time_to_city=time_to_city)


def get_monsters_from_distance_speed(distances: List[int], speeds: List[int]) -> List[Monster]:
    monsters = [Monster.from_distance_speed(distance=distances[i], speed=speeds[i]) for i in range(len(distances))]
    monsters = sorted(monsters, key=lambda m: m.time_to_city)
    return monsters


def step_minute_forward(monster: Monster) -> Monster:
    distance = monster.distance - monster.speed
    time_to_city = monster.time_to_city - 1
    return Monster(distance=distance, speed=monster.speed, time_to_city=time_to_city)


def eliminate_max(monsters: List[Monster]) -> int:
    if not monsters:
        return 0
    for monster in monsters:
        if monster.distance == 0:
            return 0
    next_monsters = [step_minute_forward(monster=monster) for monster in monsters[1:]]
    return 1 + eliminate_max(monsters=next_monsters)


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        pass


class TestEliminateMax(TestCase):
    def test_eliminate_max(self) -> None:
        distances = [1, 3, 4]
        speeds = [1, 1, 1]
        monsters = get_monsters_from_distance_speed(distances=distances, speeds=speeds)
        print(monsters)
        max_monsters = eliminate_max(monsters=monsters)
        self.assertEqual(max_monsters, 3)