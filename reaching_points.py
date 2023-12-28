import sys
from unittest import TestCase

sys.setrecursionlimit(10000)



class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        return reaching_points(sx=sx, sy=sy, tx=tx, ty=ty)


def reaching_points(sx: int, sy: int, tx: int, ty: int) -> bool:
    if sx == tx and sy == ty:
        return True
    if sx > tx:
        return False
    if sy > ty:
        return False
    x_search = reaching_points(sx=sx+sy, sy=sy, tx=tx, ty=ty)
    if x_search:
        return True
    y_search = reaching_points(sx=sx, sy=sx+sy, tx=tx, ty=ty)
    if y_search:
        return True
    return False


class TestReachingPoints(TestCase):
    def test1(self) -> None:
        result = reaching_points(sx=1, sy=1, tx=3, ty=5)
        self.assertTrue(result)

    def test2(self) -> None:
        result = reaching_points(sx=1, sy=1, tx=2, ty=2)
        self.assertFalse(result)

    def test3(self) -> None:
        result = reaching_points(sx=1, sy=1, tx=1, ty=1)
        self.assertTrue(result)

    def test4(self) -> None:
        result = reaching_points(sx=35, sy=13, tx=455955547, ty=420098884)
        self.assertTrue(result)
