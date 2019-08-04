from typing import List, Set

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

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    Build tree from pre-order and inorder traversals.
    """
    # Must specify both preorder and inorder traversals!
    if not preorder or not inorder:
        return None
    # Only one node - return it as root of subtree
    if len(preorder) == 1 and len(inorder) == 1:
        return TreeNode(preorder[0])
    # Root of tree
    root_val = preorder[0]
    root = TreeNode(root_val)
    # Left, right subtrees
    index = inorder.index(root_val)
    inorder_left = inorder[:index]
    inorder_right = inorder[index+1:]
    preorder_left = subset(preorder, set(inorder_left))
    preorder_right = subset(preorder, set(inorder_right))
    root.left = buildTree(preorder_left, inorder_left)
    root.right = buildTree(preorder_right, inorder_right)
    return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return buildTree(preorder, inorder)
