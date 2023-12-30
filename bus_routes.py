from unittest import TestCase
from typing import Dict, List, Set


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        pass


def get_stop_to_routes_dict(routes: List[List[int]]) -> Dict[int, Set[int]]:
    stop_to_routes: Dict[int, Set[int]] = {}
    for route_index, route_stops in enumerate(routes):
        for stop in route_stops:
            if stop not in stop_to_routes:
                stop_to_routes[stop] = set()
            stop_to_routes[stop].add(route_index)
    return stop_to_routes


def get_route_to_routes_dict(routes: List[List[int]]) -> Dict[int, Set[int]]:
    stop_to_routes_dict = get_stop_to_routes_dict(routes=routes)
    route_to_routes_dict: Dict[int, Set[int]] = {}
    for route_index, route_stops in enumerate(routes):
        route_to_routes_dict[route_index] = set()
        for stop in route_stops:
            new_routes = stop_to_routes_dict[stop] - {route_index}
            route_to_routes_dict[route_index] = route_to_routes_dict[route_index].union(new_routes)
    return route_to_routes_dict


def get_num_buses_to_destination(routes: List[List[int]], source: int, target: int) -> int:
    pass


class TestBuses(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.routes = [[1, 2, 7], [3, 6, 7]]
        cls.routes_long = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]

    def test1(self) -> None:
        stop_to_routes = get_stop_to_routes_dict(routes=self.routes)
        stop_to_routes_expected = {
            1: {0},
            2: {0},
            7: {0, 1},
            3: {1},
            6: {1},
        }
        self.assertEqual(stop_to_routes, stop_to_routes_expected)

    def test2(self) -> None:
        route_to_routes = get_route_to_routes_dict(routes=self.routes_long)
        route_to_routes_expected = {0: {4}, 1: {3}, 2: set(), 3: {1}, 4: {0}}
        self.assertEqual(route_to_routes, route_to_routes_expected)