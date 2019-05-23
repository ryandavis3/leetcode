import re
import copy
from typing import List
from collections import Counter

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class SubString():
    """
    Class for substring.
    """
    def __init__(self, remaining: list, start: int, L: int):
        """
        Constructor. 

        Args:
            remaining (list of str) : Words remaining to include in
                substring.
            start (int) : Index where substring starts.
            L (int) : Length of word. 
        """
        self.remaining = Counter(remaining)
        self.start = start
        self.L = L
        self.end = self.start + L
    def startRem(self):
        """
        A sort of string hash value encoding the start index and
        remaining words left.
        """
        s = '%s;' % self.start
        for key in self.remaining:
            s += '%s:%s' % (key, self.remaining[key])  
        return s

def findFirstWord(s: str, word: str) -> List[int]:
    """
    Find indices of first word. Include overlaps.
    """
    L = len(word)
    if L > 1:
        pattern = '%s(?=%s)' % (word[0], word[1:])
    else:
        pattern = word
    return [m.start() for m in re.finditer(pattern, s)]

def firstSubstrs(s: str, words: List[str]):
    """
    Find first "anchor" substrings by using the first
    word in the list.
    """
    word = words[0]
    L = len(word)
    remaining = words[1:]
    indices = findFirstWord(s, word)
    substrs = [SubString(remaining, start, L) for start in indices]
    return substrs


def extendSubstrLeft(substr: SubString, s: str) -> SubString:
    """
    Add a word to the left of the substring. Return None
    if we cannot add word.
    """
    substr = copy.deepcopy(substr)
    start_ext = substr.start - substr.L
    if start_ext >= 0:
        left_str = s[start_ext : substr.start]
        # String matches a remaining string
        if left_str in substr.remaining:
            substr.start = start_ext
            substr.remaining[left_str] -= 1
            # If no more remaining, delete key
            if substr.remaining[left_str] == 0:
                del substr.remaining[left_str]
            return substr
    return None

def extendSubstrRight(substr: SubString, s: str) -> SubString:
    """
    Add a word to the right of the substring. Return None
    if we cannot add word.
    """
    substr = copy.deepcopy(substr)
    end_ext = substr.end + substr.L
    if end_ext <= len(s):
        right_str = s[substr.end : end_ext]
        # String matches a remaining string
        if right_str in substr.remaining:
            substr.end = end_ext
            substr.remaining[right_str] -= 1
            # If no more remaining, delete key
            if substr.remaining[right_str] == 0:
                del substr.remaining[right_str]
            return substr
    return None

def extendSubstr(substr: SubString, s: str) -> List[SubString]:
    """
    Attempt to extend substring on left and right sides.
    """
    ext_left = extendSubstrLeft(substr, s)
    ext_right = extendSubstrRight(substr, s)
    ext = [ext_left, ext_right]
    ext = [x for x in ext if x is not None]
    if not ext:
        return [None]
    return ext

def extendSubstrs(substrs: List[SubString], s: str) -> List:
    """
    Attempt to extend each substring in a list. 
    
    Return two items:
    * substrs: A list of extended substrings.
    * valid_start: A list of valid start indices.
    """
    result = list()
    for substr in substrs:
        exts = extendSubstr(substr, s)
        result = result + exts
    substrs = [x for x in result if x is not None]
    valid_start = [x.start for x in substrs if not x.remaining]
    return [substrs, valid_start]

def removeDuplicateSubstrs(substrs: List[SubString]) -> List[SubString]:
    """
    Remove duplicate substrings from list.
    """    
    obs = set()
    l = list()
    for substr in substrs:
        if substr.startRem() not in obs:
            obs.add(substr.startRem())
            l.append(substr)
    return l

def buildSubstrs(substrs: List[SubString], s: str, max_substrs: int) -> List[int]:
    """
    Build substrings and find valid start points in the 
    larger string.
    """
    valid_starts = list()
    substrs = [x for x in substrs if x is not None]
    valid_starts += [x.start for x in substrs if not x.remaining]
    while len(substrs) > 0:
        [substrs, valid_start] = extendSubstrs(substrs, s)
        substrs = removeDuplicateSubstrs(substrs)
        if len(substrs) > max_substrs * 2:
            substrs = substrs[0:max_substrs]
        valid_starts = valid_starts + valid_start
    return valid_starts

def caseSingleLetter(s: str, words: List[str]):
    """
    Solve case where string and words both use only a single letter.
    """
    pass

def findSubstring(s: str, words: List[str]) -> List[int]:
    """
    Find valid starts.
    """
    # Either s or words is empty
    if not s or not words:
        return []
    # Word matches string
    if len(words) == 1 and words[0] == s:
        return [0]
    # More words than can fit in string
    Lw = len(words[0])
    if Lw * len(words) > len(s):
        return []
    # Max possible number of substrings
    max_substrs = max([len(findFirstWord(s, word)) for word in words])
    # Anchor substrings
    substrs = firstSubstrs(s, words)
    # Get substrings
    index = buildSubstrs(substrs, s, max_substrs)
    if not index:
        return []
    # Return unique indices of where word sequences can start
    index = list(set(index))
    return index

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return findSubstring(s, words)
