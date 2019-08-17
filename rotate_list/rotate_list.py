# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Alternate solution: Use a stack to search list at the
## beginning. Handle cases where k is greater than 
## the length of the list.

def rotateRight(head: ListNode, k: int) -> ListNode:
    # No node passed!
    if not k:
        return None
    # Move k places in list
    head_prev = head
    node = head
    i = 0
    while i < k:
        node = node.next
        i += 1
    # Set new tail
    tail = node
    tail.next = None
    # Set new head
    head_new = node.next
    # Find tail of original list
    while node.next:
        node = node.next
    # Append rotated part of list 
    node.next = head_prev
    return node

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        return rotateRight(head, k)   
