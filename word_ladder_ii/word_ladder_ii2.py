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
    Build adjacency list for words.
    """
    adj = {}
    for w1 in wordList:
        adj[w1] = []
        for w2 in wordList:
            if oneLetterDiff(w1, w2):
                adj[w1] += [w2]
    return adj

# Use two BFS traversals, one from begin and one from end??

# Remove words from adjacency dictionary when found so 
# they are not visited again??

# BFS one step at a time clearly defined??

def searchDJK(begin: str, end: str, words: Set):
    """
    Use Dijkstra's algorithm to find all paths from beginning
    word to end word.
    """
    dist = {}
    prev = {}
    for w in words:
        dist[w] = 10**10
        prev[w] = {}
    dist[begin] = 0
    adj = buildAdjList(words)

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
    return [dist, prev]

def recoverLadders(begin: str, end: str, prev: Dict):
    
    ladders = [[end]]
    words = [end]
    
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
    ladders = list(set([tuple(l) for l in ladders]))
    ladders = [list(l) for l in ladders]
    ladders = [l[::-1] for l in ladders]
    return ladders

class Solution:
    def findLadders(self, begin: str, end: str, words: List[str]) -> List[List[str]]:
        words = set(words)
        words.add(begin)
        if end not in words:
            return []
        [dist, prev] = searchDJK(begin, end, words)
        if not prev[end]:
            return []
        ladders = recoverLadders(begin, end, prev)
        return ladders
