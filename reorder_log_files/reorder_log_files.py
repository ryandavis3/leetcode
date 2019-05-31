from typing import List

# https://leetcode.com/problems/reorder-log-files/

def getCharsAfterIdentifier(s: str) -> str:
    """
    Get characters after identifier. Splice identifier 
    at end of string for lexicographic ordering later.
    """
    words = s.split(' ')
    return " ".join(words[1:])+words[0]

def orderLetterLogs(letter: List[str]) -> List[str]:
    """
    Order letter logs lexicopgraphically ignoring the 
    identifier. Use the identifier as a tiebreaker.
    """
    letter_tup = [tuple([l, getCharsAfterIdentifier(l)]) for l in letter]
    letter_sort = sorted(letter_tup, key=lambda x:x[1])
    letter_sort = [l[0] for l in letter_sort]
    return letter_sort

def reorderLogFiles(logs: List[str]) -> List[str]:
    """
    Reorder log files.
    """
    letter = []
    digit = []
    for _log in logs:
        words = _log.split(' ')
        if words[1].isdigit():
            digit += [_log]
        else:
            letter += [_log]
    letter = orderLetterLogs(letter)
    ordered_log = letter + digit
    return ordered_log

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return reorderLogFiles(logs)
