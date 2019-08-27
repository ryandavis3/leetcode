# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    """
    Node in singly linked list.
    """
    def __init__(self, x: int):
        self.val = x
        self.next = None

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    Given a sorted linked list, delete all duplicates
    such that each element appears only once.
    """
    # Handle cases with zero or one nodes
    if not head:
        return None
    if not head.next:
        return head
    # Maintain pointers to current and previous node
    node = head
    prev = node
    node = node.next
    # Traverse list in sequential order
    while node:
        # Found duplicate! Skip over duplicate node.
        if prev.val == node.val:
            prev.next = node.next
        else:
            prev = prev.next
        node = node.next
    return head

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return deleteDuplicates(head)
