from typing import List

# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs: List[str]) -> str:
    """
    Find the longest common prefix amongst an array of s
    strings.
    """
    # No strings passed!
    if not strs:
        return ""
    # One string passed!
    if len(strs) == 1:
        return strs[0]
    # Find max possible length of string
    L = 0
    maxL = min([len(s) for s in strs])
    if not maxL:
        return ""
    # Add characters until failure
    search = True
    while L < maxL and search:
        c = strs[0][L]
        for s in strs[1:]:
            if s[L] != c:
                search = False
                L -= 1
                break
        L += 1
    # Return longest common prefix
    return strs[0][:L]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return longestCommonPrefix(strs)
