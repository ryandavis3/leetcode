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

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return mergeTwoLists(l1, l2) 
