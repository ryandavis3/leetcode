from typing import List, Dict

# https://leetcode.com/problems/generate-parentheses

## Dynamic programming solution

def addParenthesesStr(s: str) -> List[str]:
    """
    Add parentheses to string. There are three possibilities:
        * Add () to left side
        * Add () to right side
        * Add enclosing (str)
    """
    added = []
    added += ['('+s+')']
    left = '()' + s
    right = s + '()'
    added += [left]
    if left != right:
        added += [right]
    return added

def addParenthesesList(L: List[str], D: Dict, n: int) -> List[str]:
    """
    Add parentheses to each string in a list.
    """
    L_add = []
    for s in L:
        L_add += addParenthesesStr(s)
    for num in range(2, n-1):
        for left in D[num]:
            for right in D[n-num]:
                L_add += [left+right]
        for left in D[n-num]:
            for right in D[num]:
                L_add += [left+right]
    L_add = list(set(L_add))
    return L_add

def generateParenthesis(n: int):
    """
    Generate all combinations of well-formed parentheses
    for 1, 2, up to n.
    """
    D = {}
    D[1] = ['()']
    D[2] = ['(())', '()()']
    if not n:
        return []
    elif n == 1:
        return ['()']
    elif n == 2:
        return ['(())', '()()']
    i = 2
    L = ['(())', '()()']
    while i < n:
        i += 1
        L = addParenthesesList(L, D, i)
        D[i] = L
    return L

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return generateParenthesis(n)
