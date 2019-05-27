# https://leetcode.com/problems/maximum-width-of-binary-tree/

class TreeNode:
    """
    Class for binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lrToInt(lr: str) -> int:
    """
    Convert string with characters "L", "R" to integer
    representing pos in tree. Use a bitwise 
    representation where "L"=1 and "R"=0.
    """
    lr = lr.replace('L', '0')
    lr = lr.replace('R', '1')
    return int(lr, 2)

def widthBinaryTree(root: TreeNode):
    """
    Compute the maximum width of a binary tree. 
    
    Maintain two lists as we traverse the binary tree
    one level at a time.
    * level -> nodes in level
    * pos -> position from root in L, R moves
    """
    max_W = 1
    # Position by level
    pos_by_level = list()
    pos_by_level.append(['L'])
    # Previous position and level
    prev_level = [root]
    prev_pos = ['']
    # Iterate over levels of tree
    while prev_level:
        level = list()
        pos = list()
        for i, node in enumerate(prev_level):
            node_pos = prev_pos[i]
            if node.left:
                level.append(node.left)
                pos.append(node_pos + 'L')
            if node.right:
                level.append(node.right)
                pos.append(node_pos + 'R')
        if pos:
            pos_by_level.append(pos)
            pos_int = [lrToInt(s) for s in pos]
            max_W_lev = max(pos_int) - min(pos_int) + 1
            if max_W_lev > max_W:
                max_W = max_W_lev
        prev_level = level
        prev_pos = pos
    return max_W

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return widthBinaryTree(root)
