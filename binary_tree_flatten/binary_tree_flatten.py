class TreeNode:
    """
    Class for binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inOrderTreeWalk(node: TreeNode, node_flat: TreeNode):
    """
    Perform an in-order tree walk / traveral.
    """
    if node is not None:
        node_flat.right = TreeNode(node.val)
        node_flat = node_flat.right
        node_flat = inOrderTreeWalk(node.left, node_flat)
        node_flat = inOrderTreeWalk(node.right, node_flat)
    return node_flat

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Flatten a binary tree into a linked list.
        Do not return anything, modify root in-place instead.
        """
        # User must pass a node
        if root:
            root_flatten = TreeNode(root.val)
            leaf = inOrderTreeWalk(root, root_flatten)
            root.left = None
            root.right = root_flatten.right.right
