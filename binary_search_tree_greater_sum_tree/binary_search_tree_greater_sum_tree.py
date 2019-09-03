from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bstToGst(root: TreeNode, _sum: int) -> TreeNode:
    """
    Given the root of a binary search tree with distinct values,
    modify it so every node has a new value equal to the sum 
    of the values of the original tree that are greater than
    or equal to node.val.
    """
    # Search right subtree
    if root.right:
        right = bstToGst(root.right)    
        root.val += root.right.val
    
    # Search left subtree
    if root.left:
        root.left.val += root.val 
        bstToGst(root.left)


def bstToGst2(root: TreeNode, prev_sum: int) -> List:
    """
    Given the root of a binary search tree with distinct values,
    modify it so every node has a new value equal to the sum
    of the values of the original tree that are greater than
    or equal to node.val.
    """
    if not root:
        return [None, prev_sum]

    if root.right:
        [right_node, right_sum] = bstToGst2(root.right, prev_sum)
        root.val += right_sum
    
    root.val += prev_sum
    
    prev_sum = root.val
    [left_node, left_sum] = bstToGst2(root.left, prev_sum)
    
    return [root, left_sum]

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        [root, v] = bstToGst2(root, 0)
        return root
