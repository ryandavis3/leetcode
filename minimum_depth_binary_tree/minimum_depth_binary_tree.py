from typing import List

# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    """
    Class for binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isLeaf(node: TreeNode) -> bool:
    """
    Return True if TreeNode is a leaf, else return False.
    """
    if not node.left and not node.right:
        return True
    return False

def minDepth(node: TreeNode) -> int:
    """
    Get minimum depth of tree. Use recursion on left and
    right subtrees.
    """
    # No node given!
    if not node:
        return 0
    # Node is a leaf
    if isLeaf(node):
        return 1
    # Left subtree only
    if not node.left:
        return 1 + minDepth(node.right)
    # Right subtree only
    if not node.right:
        return 1 + minDepth(node.left)
    # Left and right subtrees
    return 1 + min(minDepth(node.left), minDepth(node.right))

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return minDepth(root)
