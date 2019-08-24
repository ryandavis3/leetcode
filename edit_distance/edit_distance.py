# https://leetcode.com/problems/edit-distance/

B = 100

def minDistance(word1: str, word2: str) -> int:
    """
    Given two words word1 and word2, find the minimum number of 
    operations required to convert word1 to word2. Use the 
    Wagner-Fischer algorithm.
    """
    # Edge cases
    if not word1 and not word2:
        return 0
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)
    # Create table
    L1 = len(word1)
    L2 = len(word2)
    D = []
    for _ in range(L1+1):
        D += [[0] * (L2+1)]
    # Compare substrings to empty string
    for i in range(1, L1+1):
        D[i][0] = i
    for j in range(1, L2+1):
        D[0][j] = j
    # Complete table using recurrence
    for i in range(1, L1+1):
        for j in range(1, L2+1):
            if word1[i-1] == word2[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = min(D[i-1][j-1], D[i-1][j], D[i][j-1]) + 1
    return D[-1][-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return minDistance(word1, word2)
