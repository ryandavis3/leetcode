from typing import List

# https://leetcode.com/problems/binary-tree-inorder-traversal/

class TreeNode:
    """
    Class for node in binary tree.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root: TreeNode, L: List[int]) -> List[int]:
    """
    Perform an in-order traversal of a binary tree.
    """
    if root:
        L = inorderTraversal(root.left, L)
        L.append(root.val)
        L = inorderTraversal(root.right, L)
    return L


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        L = []
        return inorderTraversal(root, L)
