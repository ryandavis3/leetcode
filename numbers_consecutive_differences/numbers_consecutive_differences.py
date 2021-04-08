from typing import List

def numsSameConsecDiff(n: int, k: int) -> List[int]:
    
    start = [str(i) for i in range(1, 10)]

    def backtrack(N: int, arr: List[int]) -> List[int]:

        # Reached the end!
        if N == n:
            return arr

        # Subsequent numbers
        sub = []
        for val in arr:
            high = int(val[-1]) + k
            if high < 10:
                sub += [val + str(high)]
            low = int(val[-1]) - k
            if low >= 0 and k > 0:
                sub += [val + str(low)]
        
        # Backtrack
        return backtrack(N+1, sub)

    result = backtrack(1, start)
    return [int(num) for num in result]


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        return numsSameConsecDiff(n, k)


if __name__ == "__main__":
    result = numsSameConsecDiff(3, 7)
    print(result)
    result1 = numsSameConsecDiff(2, 1)
    print(result1)
    result2 = numsSameConsecDiff(2, 0)
    print(result2)
