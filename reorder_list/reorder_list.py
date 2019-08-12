# https://leetcode.com/problems/reorder-list/

class ListNode:
    """
    Node in singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def reorderList(head: ListNode) -> None:
    """
    Given a singly linked list 
        L0 -> L1 -> ... -> Ln-1 -> Ln
    reorder it to
        L0 -> Ln -> L1 -> Ln-1 -> ...

    Modify head in place.
    """
    # Edge cases -> 0, 1, or 2 nodes in list
    if not head:
        return []
    if not head.next:
        return head
    if not head.next.next:
        return head
    # Build stack using nodes in order
    stack = []
    node = head
    L = 0 # Keep track of length
    while node:
        stack += [node]
        node = node.next
        L += 1
    # Add head and tail to reordered list
    left_node = head
    right_node = stack.pop()
    left_next = left_node.next
    left_node.next = right_node
    # Add more nodes to list
    k = 2 # k is number of nodes in new list
    while k < L:
        # Even index -> add from left
        if k % 2 == 0:
            left_node = left_next
            right_node.next = left_node
            last = left_node
        # Odd index -> add from right
        else:
            left_next = left_node.next
            right_node = stack.pop()
            left_node.next = right_node
            last = right_node
        k += 1
    # Set next field of last node to None
    last.next = None
        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        reorderList(head)
