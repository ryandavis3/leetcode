from typing import List

# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode:
    """
    Node in singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists.
    """
    # Initialize root to None
    root = None
    # Iterate while we have values in either list
    while l1 or l2:
        # List 1 is empty, use list 2
        if not l1:
            node = ListNode(l2.val)
            l2 = l2.next
        # List 2 is empty, use list 1
        elif not l2:
            node = ListNode(l1.val)
            l1 = l1.next
        # Add smaller value to list
        else:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
        # If root not made yet, make it
        if not root:
            root = node
        # Update next field of previous node
        else:
            prev.next = node
        # Update previous node
        prev = node
    # Return root of new list
    return root

def passListOfLists(lists: List[ListNode]) -> List[ListNode]:
    """
    Execute one pass through a list of sorted lists where 
    we merge lists two at a time. 
    """
    L = len(lists)
    lists_merged = []
    i = 0
    while i < L:
        # Only one list left; add it
        if i == L-1:
            lists_merged += [lists[i]]
        # At least two lists left; merge next two and add result
        else:
            lists_merged += [mergeTwoLists(lists[i], lists[i+1])]
        i += 2
    return lists_merged

def mergeKLists(lists: List[ListNode]):
    """
    Merge K sorted lists using a divide and conquer approach.
    At each step combine sets of two lists to halve or nearly 
    halve the number of lists. Continue until there is only one
    list left.
    """
    if not lists:
        return []
    while len(lists) > 1:
        lists = passListOfLists(lists)
    root = lists[0]
    return root

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return mergeKLists(lists)
