from unittest import TestCase
from dataclasses import dataclass
from typing import List


def get_times_to_city_from_distance_speed(distances: List[int], speeds: List[int]) -> List[int]:
    times_to_city = [(distances[i] + 0.0) / speeds[i] for i in range(len(distances))]
    times_to_city = sorted(times_to_city)
    return times_to_city


def eliminate_max(times_to_city: List[int]) -> int:
    num_monsters = 0
    while times_to_city:
        if times_to_city[0] <= 0:
            return num_monsters
        elif times_to_city[0] >= len(times_to_city):
            return num_monsters + len(times_to_city)
        num_monsters += 1
        times_to_city = [time_to_city - 1 for time_to_city in times_to_city[1:]]
    return num_monsters


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times_to_city = get_times_to_city_from_distance_speed(distances=dist, speeds=speed)
        max_monsters = eliminate_max(times_to_city=times_to_city)
        return max_monsters


class TestEliminateMax(TestCase):
    def test_eliminate_max1(self) -> None:
        distances = [1, 3, 4]
        speeds = [1, 1, 1]
        times_to_city = get_times_to_city_from_distance_speed(distances=distances, speeds=speeds)
        max_monsters = eliminate_max(times_to_city=times_to_city)
        self.assertEqual(max_monsters, 3)

    def test_eliminate_max2(self) -> None:
        distances = [1, 1, 2, 3]
        speeds = [1, 1, 1, 1]
        times_to_city = get_times_to_city_from_distance_speed(distances=distances, speeds=speeds)
        max_monsters = eliminate_max(times_to_city=times_to_city)
        self.assertEqual(max_monsters, 1)

    def test_eliminate_max3(self) -> None:
        distances = [3, 2, 4]
        speeds = [5, 3, 2]
        times_to_city = get_times_to_city_from_distance_speed(distances=distances, speeds=speeds)
        max_monsters = eliminate_max(times_to_city=times_to_city)
        self.assertEqual(max_monsters, 1)