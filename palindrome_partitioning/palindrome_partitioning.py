from typing import List, Dict

# https://leetcode.com/problems/palindrome-partitioning/

def addPalindrome(D: Dict, s: str, start: int, end: int):
    """
    Add palindrome to dictionary. 
    """
    l = end-start+1
    if l not in D:
        D[l] = {}
    if start not in D[l]:
        D[l][start] = []
    D[l][start] += [[s[start:end+1]]]

def findPalindromes(s: str) -> Dict:
    """
    Find substrings of length at least 3 that are palindromes.
    """
    # Find palindromes of length 3
    P = []
    L = len(s)
    for i, _ in enumerate(s):
        if i == 0 or i == L-1:
            continue
        if s[i-1] == s[i+1]:
            P += [[i-1, i+1]]
    # Find palindromes of length 2
    for i, _ in enumerate(s[:-1]):
        if s[i] == s[i+1]:
            P += [[i, i+1]]
    # Attempt to extend each palindrome one letter (on each side) 
    # at a time.
    D = {}
    for pair in P:
        [start, end] = pair
        while True:
            if start < 0 or end >= L:
                break
            if s[start] != s[end]:
                break
            addPalindrome(D, s, start, end)
            start -= 1
            end += 1
    # Add palindromes of length 1 (single characters)
    D[1] = {}
    for i, char in enumerate(s):
        D[1][i] = [[char]]
    return D

def buildPartitions(D: Dict, s: str):
    """
    Build partitions using list of palindromes in place.
    """
    L = len(s)
    # Build up set of partitions using one char at a time
    for i in range(L):
        l = i+1
        if l not in D:
            D[l] = {}
        if i == 0:
            continue
        for j in range(1, i+1):
            if 0 not in D[j]:
                continue
            if j not in D[l-j]:
                continue
            if 0 not in D[l]:
                D[l][0] = []
            for s_l in D[j][0]:
                for s_r in D[l-j][j]:
                    D[l][0] += [s_l + s_r]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        L = len(s)
        D = findPalindromes(s)
        buildPartitions(D, s)
        return D[L][0]
