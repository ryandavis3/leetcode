# https://leetcode.com/problems/interleaving-string/

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    """
    Given s1, s2, s3, find whether s3 is formed by the interleaving
    of s1 and s2.
    """
    # Lengths of strings 
    L1 = len(s1)
    L2 = len(s2)
    L3 = len(s3)
    # Check string lengths are additive
    if L1 + L2 != L3:
        return False
    # At least one of the strings is empty
    if not s1:
        if s2==s3:
            return True
        else:
            return False
    if not s2: 
        if s1==s3:
            return True
        else:
            return False
    # Build empty table
    T = []
    for _ in range(L2+1):
        T += [[0] * (L1+1)]
    T[0][0] = 1
    # First row
    for j in range(1, L1+1):
        if T[0][j-1] and s1[j-1] == s3[j-1]:
            T[0][j] = 1
    # First column
    for i in range(1, L2+1):
        if T[i-1][0] and s2[i-1] == s3[i-1]:
            T[i][0] = 1
    # Fill table
    for i in range(1, L2+1):
        for j in range(1, L1+1):
            k = i + j - 1
            # Add letter from s2
            if T[i-1][j] and s2[i-1] == s3[k]:
                T[i][j] = 1
            # Add letter from s1
            if T[i][j-1] and s1[j-1] == s3[k]:
                T[i][j] = 1
    return bool(T[-1][-1]) 

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return isInterleave(s1, s2, s3)
