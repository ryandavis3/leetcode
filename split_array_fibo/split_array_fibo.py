from math import ceil
from typing import List


def splitIntoFibonacci(S: str) -> List[int]:

    # Backtracking method
    def backtrack(prev1: int, prev2: int, s: str) -> List[int]:

        # Reached end!
        next_sum = prev1 + prev2
        digits = len(str(next_sum))
        if next_sum == int(s) and digits == len(s):
            return [int(s)]

        # No leading zeroes allowed
        if digits > 1 and s[0] == "0":
            return []

        # Found next in sequence!
        if next_sum == int(s[:digits]):
            # Backtrack to subsequent elements
            sub = backtrack(prev2, next_sum, s[digits:])
            if len(sub) == 0:
                return []
            return [next_sum] + sub
        
        # No values found!
        return []

    # Iterate over starting numbers
    # First two elements uniquely determine rest of sequence
    for i in range(1, int(ceil(len(S) / 2))):
        for j in range(1, int(ceil(len(S) / 2))):
            prev1 = int(S[:i])
            prev2 = int(S[i:i+j])
            seq = backtrack(prev1, prev2, S[i+j:])
            if len(seq) > 0:
                return [prev1, prev2] + seq

    return []


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        return splitIntoFibonacci(S)


if __name__ == "__main__":
    S = "502113822114324228146342470570616913086148370223967883880490627727810157768164350462659281443027860696206741126485341822692082949177424771869507721046921249291642202139633432706879765292084310"
    result = splitIntoFibonacci(S)
    print(result)
    S = "1101111"
    result = splitIntoFibonacci(S)
    print(result)
    S = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    result = splitIntoFibonacci(S)
    print(result)
    S = "0000"
    result = splitIntoFibonacci(S)
    print(result)
    S = "11235813"
    result = splitIntoFibonacci(S)
    print(result)
    S = "123456579"
    result = splitIntoFibonacci(S)
    print(result)
    S = "112358130"
    result = splitIntoFibonacci(S)
    print(result)
