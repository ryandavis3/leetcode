from random import randint
from typing import List


LARGE_N = 10 ** 7


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.blacklist_set = set(blacklist)
        self.use_replacement = n > LARGE_N
        if not self.use_replacement:
            self.nums = [num for num in range(n) if num not in self.blacklist_set]
            self.L = len(self.nums)

    def pick_with_replacement(self) -> int:
        num = randint(0, self.n - 1)
        while num in self.blacklist_set:
            num = randint(0, self.n - 1)
        return num

    def pick_from_index(self) -> int:
        index = randint(0, self.L - 1)
        return self.nums[index]

    def pick(self) -> int:
        if self.use_replacement:
            return self.pick_with_replacement()
        else:
            return self.pick_from_index()