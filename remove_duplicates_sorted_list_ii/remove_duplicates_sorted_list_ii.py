# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode:
    """
    Node in singly linked list.
    """
    def __init__(self, x):
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
    # Traverse list in sequential order; find duplicates
    dups = set()
    while node:
        # Found duplicate! Skip over duplicate node.
        if prev.val == node.val:
            dups.add(node.val)
            prev.next = node.next
        else:
            prev = prev.next
        node = node.next
    # Move head to first non-duplicate node
    while head.val in dups and head is not None:
        head = head.next
        if head is None:
            break
    # Handle cases with zero or one nodes in new list
    if not head:
        return None
    if not head.next:
        return head
    # Maintain pointers to current and previous node
    prev = head
    node = head.next
    # Traverse list in sequential order
    while node:
        # Remove node if in duplicates list
        if node.val in dups:
            prev.next = node.next
        else:
            prev = prev.next
        node = node.next
    return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return deleteDuplicates(head)
