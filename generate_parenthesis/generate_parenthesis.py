from typing import List, Dict

# https://leetcode.com/problems/generate-parentheses

## Dynamic programming solution

def addEnclosingParentheses(s: str) -> List[str]:
    """
    Add enclosing parentheses to string.
    """
    return ['('+s+')']

def getCombinationsFromLists(L1: List[str], L2: List[str]):
    """
    Get combinations of strings from L1 (left) and
    L2 (right). String in L1 must preced string in L2.
    """
    L_comb = []
    for left in L1:
        for right in L2:
            L_comb += [left+right]
    return L_comb

def getCombinationsN(L: List[str], D: Dict, n: int) -> List[str]:
    """
    Add parentheses to each string in a list.
    """
    L_add = []
    for s in L:
        L_add += addEnclosingParentheses(s)
    for num in range(1, n):
        L_add += getCombinationsFromLists(D[num], D[n-num])
        L_add += getCombinationsFromLists(D[n-num], D[num])
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
        return D[1]
    elif n == 2:
        return D[2]
    i = 2
    L = D[2].copy()
    while i < n:
        i += 1
        L = getCombinationsN(L, D, i)
        D[i] = L
    return L

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return generateParenthesis(n)
