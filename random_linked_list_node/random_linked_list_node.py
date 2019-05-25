from random import randint

# https://leetcode.com/problems/linked-list-random-node/

class ListNode:
    """
    Class for singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def getLengthList(head: ListNode) -> int:
    """
    Get length of linked list.
    """
    node = head
    L = 0
    while node:
        L += 1
        node = node.next
    return L
   
def getNthNode(head: ListNode, N: int) -> int:
    """
    Get Nth node in linked list.
    """
    if not N:
        return head
    i = 0
    node = head
    while i < N:
        node = node.next
        i += 1
    return node

class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.L = getLengthList(head)
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        N = randint(0, self.L-1)
        node = getNthNode(self.head, N)
        return node.val

# Follow up: use reservoir sampling when the list is large.
