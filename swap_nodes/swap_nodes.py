from typing import List

# https://leetcode.com/problems/swap-nodes-in-pairs/

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

def swapPairs(head: List[ListNode]):
    """
    Given a linked list, swap every two adjacent nodes and return
    its head.
    """
    # Degenerate case - no head passed
    if not head:
        return []
    # Store linked list nodes in an array
    L = arrayOfListNodes(head)
    N = len(L)
    # Iterate through list in pairs
    A = list(range(0, N, 2))
    # Empty list for swapped nodes.
    L_swap = []
    for i in A:
        # At least two more nodes left. Make next field of second 
        # node point to first node.
        if i + 1 < N:
            node1 = L[i] 
            node2 = L[i+1]
            node2.next = node1
            L_swap += [node2, node1]
        # Only one node left. Add it to end of list.
        else:
            L_swap += [L[i]]
    # For each pair (2->1), make 1 point to the first node in the next
    # pair (4->3): 1->4
    for i in A:
        if not i:
            continue
        L_swap[i-1].next = L_swap[i]
    # Make last node next field null
    L_swap[-1].next = None
    return L_swap[0]

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return swapPairs(head)
