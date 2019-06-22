from typing import List, Set, Dict

# https://leetcode.com/problems/word-ladder/

class AdjacencyList:
    """
    Class for adjacency list with wildcard encoding
    by letter.
    """
    def __init__(self, words: Set):
        """
        Constructor. Build dict with wildcard encoding.
        e.g. D['sand'] = {'land', 'rand', 'band', 'hand', 'wand', 'sand'}
        """
        D = {}
        for word in words:
            for i in range(len(word)):
                word_st = word[0:i] + '*' + word[i+1:]
                if word_st not in D:
                    D[word_st] = set()
                D[word_st].add(word)
        self.D = D
    def get(self, word: str) -> Set:
        """
        Get adjacent words.
        """
        adj = set()
        for i in range(len(word)):
            word_st = word[0:i] + '*' + word[i+1:]
            adj = adj.union(self.D[word_st])
        adj.remove(word)
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

def bfs(beginWord: str, endWord: str, wordList: Set):
    """
    Search for target word using breadth-first search. Use
    graph abstraction. Nodes are words and two notes have
    an edge if one can be transformed to the other by
    changing only one letter.
    """
    # Adjacency list
    adj = AdjacencyList(wordList)
    # Visited nodes
    visited = set()
    visited.add(beginWord)
    # Queue for recently visited nodes
    Q = Queue()
    Q.enqueue(beginWord)
    parent = {}
    # Iterate while nodes in queue
    while not Q.is_empty:
        word = Q.dequeue()
        # End word found!
        if word == endWord:
            return parent
        # Adjacent words
        adj_words = adj.get(word)
        for adj_word in adj_words:
            if adj_word not in visited:
                parent[adj_word] = word
                visited.add(adj_word)
                Q.enqueue(adj_word)
    return None

def pathLengthParents(parent: Dict, beginWord: str, endWord: str) -> int:
    """
    Recover length of path between words from dictionary representing
    parents.
    """
    L = 1
    word = endWord
    while word != beginWord:
        L += 1
        word = parent[word]
    return L

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Given two words a dictionary's word list, find the length
    of the shortest transformation sequence from the first word to
    the second. 
    """
    wordList = set(wordList)
    wordList.add(beginWord)
    parent = bfs(beginWord, endWord, wordList)
    if parent is None:
        return 0
    return pathLengthParents(parent, beginWord, endWord)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return ladderLength(beginWord, endWord, wordList)
