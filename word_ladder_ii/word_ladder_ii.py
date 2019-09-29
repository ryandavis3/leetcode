import copy
from typing import List, Set, Dict

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
    
    # Word not available - return empty list
    if beginWord not in wordList:
        return []
    # Finished!
    if beginWord == endWord:
        return [[beginWord]]
    words = []
    words_adj = adj[beginWord]
    wordList.remove(beginWord)
    for word in words_adj:
        nextWords = search(word, endWord, wordList, adj)
        for n in nextWords:
            words += [[beginWord] + n]
    return words

def step(state: Dict, adj: Dict):

    if state['begin'] not in state['words']:
        return None
    
    if state['begin'] == state['end']:
        state['sequence'] += [state['begin']]
        state['complete'] = True
        return [state]
    
    # Adjacent words
    words_adj = adj[state['begin']]

    states_next = []
    for word in words_adj:
        if word in state['words']:
            state_next = copy.deepcopy(state)  
            state_next['words'] = state_next['words'] - {state['begin']}
            state_next['sequence'] += [state['begin']]
            state_next['begin'] = word
            states_next += [state_next]

    return states_next

# Memoize!

def steps(states: List[Dict], adj: Dict):

    print(states)
    states_next = []
    complete = False
    for state in states:
        state_next = step(state, adj)
        if state_next is not None:
            states_next += state_next
            for sn in state_next:
                if sn['complete']:
                    complete = True
    
    if complete:
        states_next = [sn for sn in states_next if sn['complete']]

    return states_next

def findLadders2(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

    wordList = set(wordList)
    wordList.add(beginWord)
    state = {'begin': beginWord, 'end': endWord, 'words': wordList, 'complete': False, 'sequence': []}
    states = [state]
    adj = buildAdjList(wordList)
    while True:
        states = steps(states, adj)
        if not states:
            return []
        if states[0]['complete']:
            states = [s['sequence'] for s in states]
            return states


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        return findLadders2(beginWord, endWord, wordList)
