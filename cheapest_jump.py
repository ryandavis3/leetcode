from dataclasses import dataclass
from unittest import TestCase
from typing import Dict, List


def is_lexicographically_smaller(path: List[int], larger_path: List[int]) -> bool:
    len_path = len(path)
    len_larger_path = len(larger_path)
    for i in range(len_path):
        if i > len_larger_path - 1:
            return False
        if path[i] < larger_path[i]:
            return True
        if path[i] > larger_path[i]:
            return False
    return True


@dataclass(frozen=True)
class Path:
    path: List[int]
    cost: int


def cheapest_jump_dp(coins: List[int], max_jump: int) -> Dict[int, Path]:
    # Initialize jumps Dict
    n_coins = len(coins)
    cheapest_jumps: Dict[int, Path] = dict()
    cheapest_jumps[0] = Path(path=[0], cost=coins[0])
    # Iterate over each coin
    for i in range(1, n_coins):
        # If not a valid coin, move to next coin
        if coins[i] == -1:
            continue
        start_j = max(0, i - max_jump)
        lowest_cost = 10 ** 10
        lowest_cost_j = None
        # Iterate over each previous step coin for jump
        for j in range(start_j, i):
            # Check we can jump from a valid coin
            if j not in cheapest_jumps:
                continue
            if cheapest_jumps[j].cost < lowest_cost:
                lowest_cost_j = j
                lowest_cost = cheapest_jumps[j].cost
            # If tie in cost, use lexicographic ordering
            elif cheapest_jumps[j].cost == lowest_cost:
                is_lex_smaller_path = is_lexicographically_smaller(
                    path=cheapest_jumps[j].path + [i],
                    larger_path=cheapest_jumps[lowest_cost_j].path + [i],
                )
                if is_lex_smaller_path:
                    lowest_cost_j = j
                    lowest_cost = cheapest_jumps[j].cost
        if lowest_cost_j is None:
            continue
        # Construct cheapest path
        cheapest_path = Path(
            path=cheapest_jumps[lowest_cost_j].path + [i],
            cost=cheapest_jumps[lowest_cost_j].cost + coins[i]
        )
        cheapest_jumps[i] = cheapest_path
    return cheapest_jumps


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        cheapest_jumps = cheapest_jump_dp(coins=coins, max_jump=maxJump)
        target_index = len(coins) - 1
        if target_index not in cheapest_jumps:
            return []
        path = cheapest_jumps[target_index].path
        path_one_indexed = [index + 1 for index in path]
        return path_one_indexed


class TestCheapestJump(TestCase):
    def test_is_lexicographically_smaller(self) -> None:
        path = [1, 2, 3]
        larger_path = [1, 2, 4]
        self.assertTrue(is_lexicographically_smaller(path=path, larger_path=larger_path))
        path = [1, 2, 3]
        larger_path = [1, 2, 3]
        self.assertTrue(is_lexicographically_smaller(path=path, larger_path=larger_path))
        path = [1, 2, 3]
        larger_path = [1, 2, 3, 4]
        self.assertTrue(is_lexicographically_smaller(path=path, larger_path=larger_path))
        path = [1, 2, 5]
        larger_path = [1, 2, 3]
        self.assertFalse(is_lexicographically_smaller(path=path, larger_path=larger_path))

    def test_cheapest_jump_dp(self) -> None:
        coins = [1, 2, 4, -1, 2]
        cheapest_jumps = cheapest_jump_dp(coins=coins, max_jump=2)
        self.assertEqual(cheapest_jumps[4], Path(path=[0, 2, 4], cost=7))

    def test_cheapest_jump_dp2(self) -> None:
        coins = [1, 2, 4, -1, 2]
        cheapest_jumps = cheapest_jump_dp(coins=coins, max_jump=1)
        self.assertFalse(4 in cheapest_jumps)

    def test_cheapest_jump_dp3(self) -> None:
        coins = [0, 0, 0, 0, 0, 0]
        cheapest_jumps = cheapest_jump_dp(coins=coins, max_jump=3)
        self.assertEqual(cheapest_jumps[5].path, [0, 1, 2, 3, 4, 5])