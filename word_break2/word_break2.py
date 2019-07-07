from typing import List, Set, Dict

# https://leetcode.com/problems/word-break-ii/

def collapseCombine(s: str, t: str) -> str:
    u = s.replace(' ', '') + t.replace(' ', '')
    return u.strip()

def memoAdd(memo: Dict, s: str, seq: str):
    if s not in memo:
        memo[s] = set()
    memo[s].add(seq)

def wordBreak(s: str, words: Set, memo: Dict, prev: str, S: List):
    # Get memoized solution
    if s in memo:
        if memo[s]:
            for subs in memo[s]:
                seq = [prev + ' ' + subs]
                strc = collapseCombine(prev, subs)
                S += seq
                memoAdd(memo, strc, seq)
            return [True, memo, S]
        else:
            return [False, memo, S]
    # Made it through full string!
    if s == '':
        strc = collapseCombine(prev, '')
        memoAdd(memo, strc, prev) 
        S += [prev]
        return [True, memo, S]
    # Build substring one letter at a time
    found = False
    for i in range(1, len(s)+1):
        subs = s[:i]
        # If substring in word dict, recursively call function
        # on remaining string.
        if subs in words:
            [valid, memo, S] = wordBreak(s[i:], words, memo, prev+' '+subs, S)
            if valid:
                memoAdd(memo, s, [subs])
                found = True
    return [found, memo, S]

def wordBreak2(s: str, words: Set, prev: str, S: List):
    # Made it through full string!
    if s == '':
        S += [prev]
        return [True, S]
    # Build substring one letter at a time
    found = False
    for i in range(1, len(s)+1):
        subs = s[:i]
        # If substring in word dict, recursively call function
        # on remaining string.
        if subs in words:
            [valid, S] = wordBreak2(s[i:], words, prev+' '+subs, S)
            if valid:
                found = True
    return [found, S]


def wordBreak3(s: str, words: Set, prev: str, S: List, memo: Dict):

    # Get memoized solution
    if True:
        if s in memo:
            subs = memo[s].copy()
            for sub in subs:
                seq = prev + ' ' + sub
                strc = collapseCombine(prev, sub)
                S += seq
                memoAdd(memo, strc, seq)
    
    # Made it through full string!
    if s == '':
        S += [prev]
        return [True, S, memo]
    
    # Build substring one letter at a time
    found = False
    for i in range(1, len(s)+1):

        subs = s[:i]
        subs_right = s[i:]

        # If substring in word dict, recursively call function
        # on remaining string.
        if subs in words:
            strc = collapseCombine(prev, subs)
            seq = prev + ' ' + subs
            memoAdd(memo, strc, seq.strip())
            [valid, S, memo] = wordBreak3(s[i:], words, prev+' '+subs, S, memo)
            if valid:
                found = True
    return [found, S, memo]


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        words = set(words)
        [valid, S] = wordBreak2(s, words, '', [])
        S = [s.strip() for s in S]
        return S
