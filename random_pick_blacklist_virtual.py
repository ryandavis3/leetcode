from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        # L is the length of the whitelist
        L = n - len(blacklist)
        # Y is the subset of the blacklist with elements larger than L
        Y = {x for x in blacklist if x >= L}
        # W is the whitelist with elements larger than L
        W = [x for x in range(L, n) if x not in Y]
        self.L = L
        self.Y = Y
        self.W = W

    def pick(self) -> int:
        pass