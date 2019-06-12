from typing import List
from collections import Counter

# https://leetcode.com/problems/group-anagrams/

def counterToStr(c: Counter) -> str:
    """
    Convert Counter to string. Make sure characters are sorted
    in alphabetical order.
    """
    chars = sorted(list(c.keys()))
    s = ""
    for char in chars:
        s += "%s:%s;" % (char, c[char])
    return s

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Given an array of strings, group anagrams together. 
    """
    ct = [Counter(s) for s in strs]
    cs = [counterToStr(c) for c in ct]
    D = {}
    N = len(strs)
    for i in range(N):
        if cs[i] not in D:
            D[cs[i]] = []
        D[cs[i]] += [strs[i]]
    return list(D.values())

## Alternatively, just each string first as a key on which 
## to index rather than making and serializing a Counter.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return groupAnagrams(strs)
