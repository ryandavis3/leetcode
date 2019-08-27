# https://leetcode.com/problems/partition-list/

class ListNode:
    """
    Node in singly linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head: ListNode, x: int) -> ListNode:
    """
    Given a linked list and a value x, partition it such that
    all nodes less than x come before nodes greater than or 
    equal to x. Preserve the original relative order of the nodes
    in each of the two partitions.
    """
    # No node passed!
    if not head:
        return None
    # Initialize left and right partitions to None
    left = None
    right = None
    # Iterate through linked list in sequential order
    node = head
    while node:
        n = ListNode(node.val)
        # Node value less than x -> left list
        if node.val < x:
            if left is not None:
                left.next = n
                left = left.next
            else:
                left = n
                left_head = left
        # Node value greater than or equal to x -> right list
        else:
            if right is not None:
                right.next = n
                right = right.next
            else:
                right = n
                right_head = right
        node = node.next
    # Splice partitions together
    if left is not None and right is not None:
        left.next = right_head
        return left_head
    elif left is None:
        return right_head
    else:
        return left_head

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        return partition(head, x)
