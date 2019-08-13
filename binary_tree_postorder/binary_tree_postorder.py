from typing import List

# https://leetcode.com/problems/binary-tree-postorder-traversal/

class TreeNode:
    """
    Binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorder(node: TreeNode) -> List[int]:
    """
    Recursively perform a postorder traversal of a tree's nodes.
    """
    if not node:
        return []
    return  postorder(node.left) + postorder(node.right) + [node.val]

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return postorder(root)
