from random import randint
from typing import List
from unittest import TestCase


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        # L is the length of the whitelist
        L = n - len(blacklist)
        # Y is the subset of the blacklist with elements greater than L
        Y = {x for x in blacklist if x >= L}
        # W is the whitelist with elements greater than L
        W = [x for x in range(L, n) if x not in Y]
        # X is the subset of the blacklist with elements less than L
        X = [x for x in blacklist if x < L]
        # M is the virtual whitelist
        M: Dict[int, int] = dict()
        for i, num in enumerate(X):
            M[num] = W[i]
        self.M = M
        self.L = L

    def pick(self) -> int:
        # Get a random index
        index = randint(0, self.L - 1)
        # Return value in virtual whitelist at key corresponding to index.
        # If key not in whitelist, return key as value.
        return self.M.get(index, index)


class TestSolution(TestCase):
    def test1(self) -> None:
        blacklist = [2, 3, 5]
        solution = Solution(n=7, blacklist=blacklist)
        solution.pick()
        solution.pick()
        solution.pick()