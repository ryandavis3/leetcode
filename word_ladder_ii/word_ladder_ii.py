import copy
from typing import List, Set

# https://leetcode.com/problems/word-ladder-ii/

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    """
    Given two words and a dictionary's word list, find all transformation
    sequence(s) such that only one letter can be changed at a time
    and each transformed word must exist in the word list.
    """
    # Return empty list if beginning / end words not in word list
    wordList = set(wordList)
    wordList.add(beginWord)
    adj = buildAdjList(wordList)
    words = search(beginWord, endWord, wordList, adj)
    if not words: 
        return []
    words.sort(key=len)
    L = len(words[0])
    return [w for w in words if len(w) == L]

# Use a radix tree to solve??
# Try using BFS first?? 

def oneLetterDiff(a: str, b: str) -> bool:
    """
    Return True if strings a and b have exactly one 
    letter different.
    """
    diff = 0
    for i, c in enumerate(a):
        if diff > 1:
            return False
        if b[i] != c:
            diff += 1
    if diff == 1:
        return True
    return False

def buildAdjList(wordList: Set):
    """
    Build adjacency list for words.
    """
    adj = {}
    for w1 in wordList:
        adj[w1] = []
        for w2 in wordList:
            if oneLetterDiff(w1, w2):
                adj[w1] += [w2]
    return adj


def search(beginWord: str, endWord: str, wordList: Set, adj: Set) -> List[List[str]]:

    if beginWord not in wordList:
        return []

    # Finished!
    if beginWord == endWord:
        return [[beginWord]]
    
    words = []
    words_adj = adj[beginWord]

    wordList = copy.deepcopy(wordList)
    wordList.remove(beginWord)

    for word in words_adj:
        nextWords = search(word, endWord, wordList, adj)
        for n in nextWords:
            words += [[beginWord] + n]

    return words

    
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        return findLadders(beginWord, endWord, wordList)
