def arrangeCoins(n: int) -> int:
    if n == 0:
        return 0
    steps = 0
    total = 0
    while total + steps <= n:
        total += steps
        steps +=1
    return total

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return arrangeCoins(n)
