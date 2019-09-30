import copy
from typing import List, Set, Dict

# https://leetcode.com/problems/word-ladder-ii/

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
    Build adjacency list for words. Two words are adjacent if
    they differ by exactly one character.
    """
    adj = {}
    for w1 in wordList:
        adj[w1] = set()
        for w2 in wordList:
            if oneLetterDiff(w1, w2):
                adj[w1].add(w2)
    return adj

# Use two BFS traversals, one from begin and one from end??

# BFS one step at a time clearly defined??

def search(begin: str, end: str, words: Set):
    """
    Use Dijkstra's algorithm to find all paths from beginning
    word to end word.
    """
    # Dictionaries for distance from beginning word and 
    # previous word in path.
    dist = {}
    prev = {}
    for w in words:
        dist[w] = 10**10
        prev[w] = {}
    dist[begin] = 0
    # Word adjacency list 
    adj = buildAdjList(words)
    # Traverse graph
    Q = [begin]
    while Q:
        word = Q.pop(0)
        for aw in adj[word]:
            alt = dist[word] + 1
            if alt < dist[aw]:
                dist[aw] = alt
                prev[aw] = {word}
                Q += [aw]
            elif alt == dist[aw]:
                prev[aw].add(word)
                Q += [aw]
        removeWordAdj(adj, word)
    # Return completed distance and previous word dicts
    return [dist, prev]

def recoverLadders(begin: str, end: str, prev: Dict):
    """
    Recover paths from beginning word to end word using 
    predecessor words.
    """
    # Start with end word
    ladders = [[end]]
    words = [end]
    # Fill out ladders until we reach beginning word
    complete = False
    while not complete:
        ladders_next = []
        words_next = []
        for i, ladder in enumerate(ladders):
            pws = prev[words[i]]
            for pw in pws:
                ladders_next += [ladder + [pw]]
                words_next += [pw]
                if pw == begin:
                    complete = True
        ladders = ladders_next
        words = words_next
    # Get unique paths, reverse order
    ladders = list(set([tuple(l) for l in ladders]))
    ladders = [list(l) for l in ladders]
    ladders = [l[::-1] for l in ladders]
    return ladders

def removeWordAdj(adj: Dict, word):
    """
    Remove word from adjacency lists.
    """
    for w in adj:
        if word in adj[w]:
            adj[w].remove(word)

def findLadders(self, begin: str, end: str, words: List[str]) -> List[List[str]]:
    """
    Given two words (begin and end) and a dictionary's word list, find
    all shortest transformation sequence(s) such that only one
    letter can be changed at a time and each transformed word must 
    exist in the word list.
    """
    # Represent word list as set rather than list
    words = set(words)
    words.add(begin)
    # End word not in list! No possible paths!
    if end not in words:
        return []
    # Find all paths in word "graph"
    [dist, prev] = search(begin, end, words)
    # Did not reach end -> return empty list
    if not prev[end]:
        return []
    # Recover ladders from predecessors
    ladders = recoverLadders(begin, end, prev)
    return ladders

class Solution:
    def findLadders(self, begin: str, end: str, words: List[str]) -> List[List[str]]:
        return findLadders(begin, end, words)
