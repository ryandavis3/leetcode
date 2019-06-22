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
        if n_edits > 1:
            return False
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

class Queue:
    """
    Class implementing queue (LIFO).
    """
    def __init__(self):
        self.Q = []
    def enqueue(self, value):
        self.Q = self.Q + [value]
    def dequeue(self):
        value = self.Q[0]
        self.Q = self.Q[1:]
        return value
    @property
    def is_empty(self):
        return len(self.Q) == 0

def bfs(word: str, adj: Dict, target: str):
    """
    Search for target word using breadth-first search. Use
    graph abstraction. Nodes are words and two notes have
    an edge if one can be transformed to the other by
    changing only one letter.
    """
    # Visited nodes
    visited = set()
    visited.add(word)
    # Queue for recently visited nodes
    Q = Queue()
    Q.enqueue(word)
    parent = {}
    # Iterate while nodes in queue
    while not Q.is_empty:
        word = Q.dequeue()
        # Target found!
        if word == target:
            return parent
        # Adjacent words
        adj_words = adj[word]
        for adj_word in adj_words:
            if adj_word not in visited:
                parent[adj_word] = word
                visited.add(adj_word)
                Q.enqueue(adj_word)
    return None

def bfsFast(word: str, words: Set, target: str):
    """
    Faster (by a constant factor) breadth-first search.
    """
    visited = set()
    visited.add(word)
    unvisited = words.copy()
    Q = Queue()
    Q.enqueue(word)
    parent = {}
    while not Q.is_empty:
        word = Q.dequeue()
        if word == target:
            return parent
        adj_words = getAccessibleWords(word, unvisited)
        for adj_word in adj_words:
            if adj_word not in visited:
                parent[adj_word] = word
                visited.add(adj_word)
                unvisited.remove(adj_word)
                Q.enqueue(adj_word)


def pathLengthParents(parent: Dict, start: str, end: str) -> int:
    """
    Recover length of path between words from dictionary representing
    parents.
    """
    L = 1
    word = end
    while word != start:
        L += 1
        word = parent[word]
    return L

def ladderLength(start: str, end: str, words: List[str]) -> int:
    """
    Given two words a dictionary's word list, find the length
    of the shortest transformation sequence from the first word to
    the second. 
    """
    words = set(words)
    words.add(start)
    adj = getAdjacencyLists(words)
    parent = bfs(start, adj, end)
    if parent is None:
        return 0
    return pathLengthParents(parent, start, end)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return ladderLength(beginWord, endWord, wordList)
