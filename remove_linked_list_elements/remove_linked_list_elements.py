class ListNode:
    """
    Class for node in singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        Remove elements in linked list whose value equals val.
        """
        # Case where linked list is empty
        if not head:
            return []
        # Case with one node in linked list
        if head.next is None:
            if head.val == val:
                return []
            else:
                return head
        # Case with at least two nodes
        # Remove nodes at beginning of list
        while head.val == val:
            head = head.next
            if head is None:
                return []
        prev = head
        node = head.next
        # Begin from second node
        while node is not None:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        # Return head of list with nodes removed
        return head
