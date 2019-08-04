from typing import List, Set

# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class TreeNode:
    """
    Binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def subset(L: List[int], S: Set[int]) -> List:
    """
    Get integers in list L (preserving order) that are
    in set S.
    """
    return [val for val in L if val in S]

def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    """
    Build tree from inorder and postorder traversals.
    """
    # Must specify both postorder and inorder traversals!
    if not postorder or not inorder:
        return None
    root_val = postorder[-1]
    # Only one node - return it as root of subtree
    if len(postorder) == 1 and len(inorder) == 1:
        return TreeNode(root_val)
    # Root of tree
    root = TreeNode(root_val)
    # Left, right subtrees
    index = inorder.index(root_val)
    inorder_left = inorder[:index]
    inorder_right = inorder[index+1:]
    postorder_left = subset(postorder, set(inorder_left))
    postorder_right = subset(postorder, set(inorder_right))
    root.left = buildTree(inorder_left, postorder_left)
    root.right = buildTree(inorder_right, postorder_right)
    return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return buildTree(inorder, postorder)
