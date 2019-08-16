# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s: str) -> int:
    """
    Return the length of the last word in a string. Return 
    zero if the last word does not exist.
    """
    if not s:
        return 0
    s_split = s.split()
    if not s_split:
        return 0
    return len(s_split[-1])

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return lengthOfLastWord(s)
