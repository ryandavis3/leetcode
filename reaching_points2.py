from unittest import TestCase


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        return reaching_points(sx=sx, sy=sy, tx=tx, ty=ty)


def reaching_points(sx: int, sy: int, tx: int, ty: int) -> bool:
    # Iterate while we can still subtract
    while tx >= sx and ty >= sy:
        if tx == ty:
            break
        # tx larger, subtract ty
        if tx > ty:
            # Cannot decrease ty further -> check if it works with tx
            if ty <= sy:
                return (tx - sx) % ty == 0
            else:
                tx %= ty
        # ty larger, subtract tx
        else:
            # Cannot decrease tx further -> check if it works with ty
            if tx <= sx:
                return (ty - sy) % tx == 0
            else:
                ty %= tx
    return sx == tx and sy == ty


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
        self.assertFalse(result)
