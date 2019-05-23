import re
import copy
from typing import List
from collections import Counter

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Represent left words as Counter for O(1) lookup
# Be able to handle cases with duplicate words, e.g.
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]
# should get result of [8]

class SubString():
    """
    Class for substring.
    """
    def __init__(self, found: set, left: set, start: int, L: int):
        self.found = found
        self.left = left
        self.start = start
        self.L = L
        self.end = self.start + L
    

def findFirstWord(s: str, word: str) -> List[int]:
    """
    Find indices of first word.
    """
    return [m.start() for m in re.finditer(word, s)]

def firstSubstrs(s: str, words: List[str]):
    """
    Find first "anchor" substrings by using the first
    word in the list.
    """
    word = words[0]
    L = len(word)
    found = set([words[0]])
    left = set(words[1:])
    indices = findFirstWord(s, word)
    substrs = [SubString(found, left, start, L) for start in indices]
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
        if left_str in substr.left:
            substr.start = start_ext
            substr.left.remove(left_str)
            substr.found.add(left_str)
            return substr
    return None

def extendSubstrRight(substr: SubString, s: str) -> SubString:
    """
    Add a word to the right of the substring. Return None
    if we cannot add word.
    """
    substr = copy.deepcopy(substr)
    end_ext = substr.end + substr.L
    if end_ext < len(s):
        left_str = s[substr.end : end_ext]
        if left_str in substr.left:
            substr.end = end_ext
            substr.left.remove(left_str)
            substr.found.add(left_str)
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
    valid_start = [x.start for x in substrs if not x.left]
    return [substrs, valid_start]

def buildSubstrs(substrs: List[SubString], s: str) -> List[int]:
    """
    Build substrings and find valid start points in the 
    larger string.
    """
    valid_starts = list()
    while len(substrs) > 0:
        [substrs, valid_start] = extendSubstrs(substrs, s)
        valid_starts = valid_starts + valid_start
    return valid_starts

def findSubstring(s: str, words: List[str]) -> List[int]:
    """
    Find valid starts.
    """
    if not s or not words:
        return []
    substrs = firstSubstrs(s, words)
    index = buildSubstrs(substrs, s)
    if not index:
        return []
    index = list(set(index))
    return index

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return findSubstring(s, words)
