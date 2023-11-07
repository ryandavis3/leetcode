from unittest import TestCase
from typing import Dict, List


def get_least_bricks(wall: List[List[int]]) -> int:
    # Counter for edge positions
    edge_positions_counter: Dict[int, int] = {}
    # Length and height of wall
    len_wall = sum(wall[0])
    height_wall = len(wall)
    # Iterate over each row in wall
    for row in wall:
        # Iterate over each brick in the row
        edge_position = 0
        for brick in row:
            # Use running tracker of cumulative edge position
            edge_position += brick
            if edge_position == len_wall:
                continue
            if edge_position not in edge_positions_counter:
                edge_positions_counter[edge_position] = 0
            edge_positions_counter[edge_position] += 1
    # All bricks cover the entire length
    if not edge_positions_counter:
        return height_wall
    edge_position_counts = set(edge_positions_counter.values())
    # Cross least bricks where there are the most edge position counts
    return height_wall - max(edge_position_counts)



class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        return get_least_bricks(wall=wall)


class TestLeastBricks(TestCase):

    def test1(self) -> None:
        wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
        least_bricks = get_least_bricks(wall=wall)
        self.assertEqual(least_bricks, 2)

    def test2(self) -> None:
        wall = [[1],[1],[1]]
        least_bricks = get_least_bricks(wall=wall)
        self.assertEqual(least_bricks, 3)