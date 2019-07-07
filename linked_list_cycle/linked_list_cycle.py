# https://leetcode.com/problems/linked-list-cycle

class ListNode(object):
    """
    Class for singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    """
    Return True if linked list with head has a cycle, else
    return False.
    """
    # Two pointers to head of list. A slow pointer
    # moves one node at a time while a fast pointer
    # moves two nodes at a time.
    slow = head
    fast = head
    while slow:
        if not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
        if not slow or not fast:
            return False
        if slow.val == fast.val:
            return True
    return False

class Solution(object):
    def hasCycle(self, head):
        return hasCycle(head)     
