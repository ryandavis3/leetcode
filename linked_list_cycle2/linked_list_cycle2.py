# https://leetcode.com/problems/linked-list-cycle-ii/

class ListNode(object):
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    """
    Given a linked list, return the node where the cycle begins.
    If there is no cycle, return None.
    """
    D = set()
    while head:
        # If head found in visited nodes, return it.
        if head in D:
            return head
        D.add(head)
        head = head.next
    # Reached end of list without cycle
    return None

class Solution(object):
    def detectCycle(self, head):
        return detectCycle(head)
