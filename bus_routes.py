from unittest import TestCase
from typing import Dict, List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        pass


def get_stop_to_routes_dict(routes: List[List[int]]) -> Dict[int, List[int]]:
    stop_to_routes: Dict[int, List[int]] = {}
    for route_index, route_stops in enumerate(routes):
        for stop in route_stops:
            if stop not in stop_to_routes:
                stop_to_routes[stop] = list()
            stop_to_routes[stop].append(route_index)
    return stop_to_routes


def get_num_buses_to_destination(routes: List[List[int]], source: int, target: int) -> int:
    pass


class TestBuses(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.routes = [[1, 2, 7], [3, 6, 7]]

    def test1(self) -> None:
        stop_to_routes = get_stop_to_routes_dict(routes=self.routes)
        stop_to_routes_expected = {
            1: [0],
            2: [0],
            7: [0, 1],
            3: [1],
            6: [1],
        }
        self.assertEqual(stop_to_routes, stop_to_routes_expected)