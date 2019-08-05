from typing import Set

# https://leetcode.com/problems/path-sum/submissions/

class TreeNode:
    """
    Binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isLeaf(node: TreeNode) -> bool:
    """
    Return True if node is leaf, else return False.
    """
    if not node.left and not node.right:
        return True
    return False

def pathSum(root: TreeNode, val: int) -> bool:
    """
    Return True if tree has a root-to-leaf path
    such that adding up the values along the path equals
    the given sum.
    """
    # No node given
    if not root:
        return False
    # If node value match and node is leaf, found path
    if root.val == val and isLeaf(root):
        return True
    # Check left and right subtrees
    sub_val = val - root.val
    left = pathSum(root.left, sub_val)
    right = pathSum(root.right, sub_val)
    return max(left, right)


class Solution:
    def hasPathSum(self, root: TreeNode, val: int) -> bool:
        return pathSum(root, val)
