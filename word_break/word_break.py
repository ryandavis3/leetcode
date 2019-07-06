from typing import List, Set, Dict

# https://leetcode.com/problems/word-break/

def wordBreak(s: str, words: Set, memo: Dict):
    """
    Given a string s and a set of words, determine if s
    can be segmented into a space-separated sequence of
    one or more dictionary words. Use recursion and memoize.
    """
    # Get memoized solution
    if s in memo:
        return [memo[s], memo]
    # Made it through full string!
    if s == '':
        memo[s] = True
        return [True, memo]
    # Build substring one letter at a time
    for i in range(1, len(s)+1):
        subs = s[:i]
        # If substring in word dict, recursively call function
        # on remaining string.
        if subs in words:
            [valid, memo] = wordBreak(s[i:], words, memo)
            if valid:
                memo[s] = True
                return [True, memo]
    # No sequence found - return False
    memo[s] = False
    return [False, memo]

class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        memo = {}
        words = set(words)
        [seq, memo] = wordBreak(s, words, memo)
        return seq
