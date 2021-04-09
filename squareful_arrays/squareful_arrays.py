from typing import List, Dict
from math import sqrt
from collections import Counter


def numSquarefulPerms(A: List[int]) -> int:

    if set(A) == {2}:
        return 1

    count = dict(Counter(A))

    def backtrack(last: int, remain: Dict[int, int]) -> List[int]:

        # Remove zeroes
        remain = {k:v for k, v in remain.items() if v > 0}

        # Reached the end!
        last_num = list(remain.keys())[0]
        last_ct = list(remain.values())[0]
        if len(remain) == 1 and sqrt(last + last_num) % 1 == 0 and last_ct == 1:
            return [[last_num]]
            
        # Iterate over remaining values 
        sub = []
        for val, ct in remain.items():
            
            # Adjacent values are squareful
            if sqrt(last + val) % 1 == 0:
                remain_next = remain.copy()
                remain_next[val] -= 1
                
                # Backtrack and add 
                new = backtrack(val, remain_next)
                if len(new) > 0:
                    for n in new:
                        sub += [[val] + n]

        return sub
   
    # Iterate over start values
    results = []
    for index, val in enumerate(A):
        remain = count.copy()
        remain[val] -= 1
        subs = backtrack(val, remain)
        results += [[val] + sub for sub in subs]

    tups = [tuple(l) for l in results]
    unique = set(tups)
    return len(unique)


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        return numSquarefulPerms(A)


if __name__ == "__main__":
    A = [0,0,0,0,0,0,1,1,1,1,1,1]
    result = numSquarefulPerms(A)
    print(result)
    A = [2,2,2,2,2,2,2,2,2,2]
    result3 = numSquarefulPerms(A)
    print(result3)
    A = [2,2]
    result2 = numSquarefulPerms(A)
    print(result2)
    A = [1,17,8]
    result = numSquarefulPerms(A)
    print(result)
    A = [2, 2, 2]
    result1 = numSquarefulPerms(A)
    print(result1)
