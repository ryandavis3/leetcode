from typing import List

# https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode:
    """
    Node in singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def listFromArray(array: List[int]) -> ListNode:
    """
    Make a linked list from an array. Return the head of the
    array. Return the head of the list.
    """
    head = ListNode(array[0])
    node = head
    for val in array[1:]:
        node.next = ListNode(val)
        node = node.next
    return head

def arrayOfListNodes(head: ListNode) -> List[ListNode]:
    """
    Make an array of linked list nodes.
    """
    L = []
    node = head
    while node:
        L += [node]
        node = node.next
    return L

def printNodes(head: ListNode) -> None:
    """
    Print nodes in linked list.
    """
    node = head
    while node:
        print(node.val)
        node = node.next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    """
    Given a linked list, reverse the nodes of a linked list
    k at a time and return its modified list.
    """
    # Degenerate case - no head passed
    if not head:
        return []
    # Store linked list nodes in an array
    L = arrayOfListNodes(head)
    N = len(L)
    # Iterate through list in pairs
    A = list(range(0, N, k))
    # Empty list for swapped nodes.
    L_swap = []
    for i in A:
        # At least k more nodes left.
        if i + k <= N:
            Li = []
            prev = L[i]
            Li = [prev] + Li
            for j in range(1, k):
                node = L[i+j]
                node.next = prev
                Li = [node] + Li
                prev = node
            L_swap += Li
        # Less than k nodes left; add to list
        else:
            L_swap += L[i:]
    for i in A:
        if not i:
            continue
        L_swap[i-1].next = L_swap[i]
    # Make last node next field null
    L_swap[-1].next = None
    return L_swap[0]

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return reverseKGroup(head, k)        
