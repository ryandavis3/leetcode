from typing import List

# https://leetcode.com/problems/binary-tree-preorder-traversal/

class TreeNode:
    """
    Binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder(node: TreeNode) -> List[int]:
    """
    Recursively perform a preorder traversal of a tree's nodes.
    """
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return preorder(root)
