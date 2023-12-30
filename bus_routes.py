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


def get_buses_to_target(source: int, target: int, route_to_routes_dict: Dict[int, Set[int]], prev_routes: Set[int]) -> int:
    if source == target:
        return 0
    possible_routes = route_to_routes_dict[source] - prev_routes
    if not possible_routes:
        return -1
    if target in possible_routes:
        return 1
    prev_routes = prev_routes.union(set([source]))
    paths = [get_buses_to_target(source=route, target=target, route_to_routes_dict=route_to_routes_dict, prev_routes=prev_routes) for route in possible_routes]
    reachable_paths = [path for path in paths if path >= 0]
    if not reachable_paths:
        return -1
    return 1 + min(reachable_paths)


def get_num_buses_to_destination(routes: List[List[int]], source: int, target: int) -> int:
    pass


class TestBuses(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.routes = [[1, 2, 7], [3, 6, 7]]
        cls.routes_long = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
        cls.route_to_routes_long = {0: {4}, 1: {3}, 2: set(), 3: {1}, 4: {0}}

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

    def test3(self) -> None:
        buses = get_buses_to_target(source=2, target=0, route_to_routes_dict=self.route_to_routes_long, prev_routes=set())
        self.assertEqual(buses, -1)
        buses = get_buses_to_target(source=0, target=4, route_to_routes_dict=self.route_to_routes_long,
                                    prev_routes=set())
        self.assertEqual(buses, 1)

