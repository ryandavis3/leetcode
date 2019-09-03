from typing import List

class TreeNode:
    """
    Binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstToGst(root: TreeNode, prev_sum: int) -> int:
    """
    Given the root of a binary search tree with distinct values,
    modify it so every node has a new value equal to the sum
    of the values of the original tree that are greater than
    or equal to node.val.

    Perform a reverse inorder traversal.
    """
    # Search right subtree
    if root.right:
        root.val += bstToGst(root.right, prev_sum)
    else:
        root.val += prev_sum
    # Search left subtree
    if root.left:
        left_sum = bstToGst(root.left, root.val)
    else:
        left_sum = root.val
    # Return sum of entire subtree to parent
    return left_sum

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val = bstToGst(root, 0)
        return root
