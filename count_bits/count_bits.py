from typing import List

def countBits(num: int) -> List[int]:
    bits = [0, 1]
    n = 2
    while n - 1 < num:
        bits_extend = [b + 1 for b in bits]
        n *= 2
        bits += bits_extend
    return bits[:num+1]


class Solution:
    def countBits(self, num: int) -> List[int]:
        return countBits(num)


if __name__ == "__main__":
    result = countBits(2)
    print(result)
    result = countBits(5)
    print(result)
