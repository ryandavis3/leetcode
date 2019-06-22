from typing import List, Set, Dict

# https://leetcode.com/problems/word-ladder/

def isAccessible(word1: str, word2: str) -> bool:
    """
    Return True if we can obtain word2 by changing at most one
    letter from word1. Else return False.
    """
    if word1 == word2:
        return False
    L = len(word1)
    n_edits = 0
    for i in range(L):
        if word1[i] != word2[i]:
            n_edits += 1
    return n_edits == 1

def getAccessibleWords(word: str, words: Set) -> Set:
    """
    Get words from list that are accessible from a starting
    word. 
    """
    words_a = set()
    for word_tf in words:
        if isAccessible(word, word_tf):
            words_a.add(word_tf)
    return words_a

def getAdjacencyLists(words: Set) -> Dict:
    """
    Get adjacency lists for set of words.
    """
    adj = {}
    for word in words:
        adj[word] = getAccessibleWords(word, words)
    return adj 

## Use breadth-first search to find the shortest path between
## the two words.

## Keep set of discovered words

## https://en.wikipedia.org/wiki/Breadth-first_search

## If end word not on list, return False right away

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass
