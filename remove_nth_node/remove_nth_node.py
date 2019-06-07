# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    """
    Node in singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    Remove nth node from end of a linked list. Solve in one pass.
    """
    if not head.next and n == 1:
        return []
    # Maintain two pointers. Move the first n+1 nodes ahead 
    # of the original head.
    node_front = head
    L = [node_front]
    for i in range(n+1):
        node_front = node_front.next
    # Second pointer is behind
    node_back = head
    # Move two pointers at the same rate forward
    while node_front:
        node_front = node_front.next
        node_back = node_back.next
    # Update next field in back node to "skip" a node
    node_back.next = node_back.next.next
    return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
       return removeNthFromEnd(head, n) 
