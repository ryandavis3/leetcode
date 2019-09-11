class ListNode:
    """
    Node in singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    """
    Reverse a linked list from position m to n in one pass.
    """
    # No list passed!
    if not head:
        return []
    # Only one node passed!
    if not head.next:
        return head
    # Two nodes in list!
    if not head.next.next:
        # Reverse first and second nodes
        if m == 1 and n == 2:
            node2 = head.next
            node2.next = head
            head.next = None
            head = node2
        return head
    # Start and end indices are same!
    if m == n:
        return head
    # Move head to first node in list to reverse
    prev = head
    curr = prev.next
    i = 1
    while i < m:
        i += 1
        prev = prev.next
        curr = curr.next
    # Iteratively reverse linked list
    prev_tail = prev
    curr_tail = curr
    while i < n and curr:
        ptr = curr
        curr = curr.next
        ptr.next = prev
        prev = prev.next
    # Stitch list together
    prev_tail.next = ptr
    curr_tail.next = curr
    return head

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        return reverseBetween(head, m, n)    
