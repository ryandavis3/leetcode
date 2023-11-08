from unittest import TestCase


def is_reachable(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    x_diff = abs(sx - fx)
    y_diff = abs(sy - fy)
    if max(x_diff, y_diff) <= t:
        return True
    return False


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        pass


class TestReachable(TestCase):

    def test1(self) -> None:
        reachable_result = is_reachable(sx=2, sy=4, fx=7, fy=7, t=6)
        self.assertTrue(reachable_result)

    def test2(self) -> None:
        reachable_result = is_reachable(sx=3, sy=1, fx=7, fy=3, t=3)
        self.assertFalse(reachable_result)