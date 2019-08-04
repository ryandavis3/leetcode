from typing import List

# https://leetcode.com/problems/balanced-binary-tree/

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

def depth(root: TreeNode):
    """
    Get depth of tree. If tree is not height-balanced, 
    return -1.
    """
    # No node passed!
    if not root:
        return 0
    # Node is a leaf
    if isLeaf(root):
        return 1
    # Recursively get depth of left and right subtrees
    left = depth(root.left)
    right = depth(root.right)
    # If subtree is not balanced, tree is not balanced
    if left < 0 or right < 0:
        return -1
    # Check if depths of two subtrees differ by more than one
    if abs(left - right) > 1:
        return -1
    return 1 + max(left, right)

def isBalanced(root: TreeNode) -> bool:
    """
    Return True if binary tree is balanced, else return False.
    """
    depth_tree = depth(root)
    if depth_tree < 0:
        return False
    return True

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return isBalanced(root)
