from typing import List

# https://leetcode.com/problems/combinations/

def combine(n: int, k: int) -> List[List[int]]:

    # k = 1 case
    C = []
    for i in range(1, n+1):
        C += [[i]]
    # Build on solution for larger k
    r = 2
    while r <= k:
        D = []
        for c in C:
            # Add number to each set
            num = r
            while num <= n:
                D += [c + [num]]
                num += 1
            r += 1
        C = D
    return C

def combine2(n: int, k: int) -> List[List[int]]:

    # k = 1 case
    C = {}
    for i in range(1, n+1):
        C[i] += [[i]]
    # Build on solution for larger k
    r = 2
    while r <= k:
        D = {}
        keys = sorted(C.values)
        for key in keys:
            # Add number to each set
            D[key] = []
            values = C[key]
            num = key + (r - 1)
            while num <= n:
                D += [C[key] + [num]]
                num += 1
            r += 1
        C = D
    return C

def combine3(n: int, k: int) -> List[List[int]]:

    # k = 1 case
    C = []
    for i in range(1, n+1):
        C += [[i]]
    # Build on solution for larger k
    r = 2
    while r <= k:
        D = []
        start = -1
        offset = r-1
        offset2 = 0
        pos = 0
        prev = -1
        for c in C:
            
            prev_i = -min(2, len(c))
            if c[0] != start:
                start = c[0]
                prev = c[prev_i]
                offset += 1
                offset2 = 0
                pos = 0
            elif c[prev_i] != prev:
                offset2 += 1
                prev = c[prev_i]
                pos = 0
            else:
                #offset = r
                pos += 1

            print('c : %s' % c)
            print('offset: %s' % offset)
            print('offset2: %s' % offset2)
            print('pos: %s' % pos)

            # Add number to each set
            num = offset + offset2 + pos
            #print(num) 
            #if num <= n:
            #    D += [c + [num]]
            #num += 1

            while num <= n:
                D += [c + [num]]
                num += 1
        r += 1
        C = D
    return C

def combine4(n: int, k: int, md: int) -> List[List[int]]:
    if k == 0:
        return [[]]
    combs = []
    for ld in range(md, n+1):
        rds = combine4(n, k-1, ld+1)
        for rd in rds:
            combs += [[ld] + rd]
    return combs


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combine4(n, k)
