from typing import List

# https://leetcode.com/problems/merge-k-sorted-lists/solution/

class ListNode:
    """
    Node in a singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def arrayToLinkedList(array: List[int]) -> List[ListNode]:
    """
    Make a linked list from an array.
    """
    L = len(array)
    nodes = [ListNode(val) for val in array]
    for i, node in enumerate(nodes):
        if i + 1 < L:
            node.next = nodes[i+1]
    root = nodes[0]
    return root

def arraysToLinkedLists(arrays: List[List[int]]) -> List[ListNode]:
    """
    Make several linked lists from several arrays.
    """
    return [arrayToLinkedList(array) for array in arrays]

def takeSecond(elem):
    """
    Take second element in list, array, tuple.
    """
    return elem[1]

def getValsFromRoots(lls: List[ListNode]):
    """
    Get values of nodes from roots of sorted lists.
    """
    vals = []
    for i, root in enumerate(lls):
        vals.append(tuple([i, root.val]))
    vals = sorted(vals, key=takeSecond)
    return vals

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass        
