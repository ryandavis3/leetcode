from typing import List

# https://leetcode.com/problems/sum-root-to-leaf-numbers/

class TreeNode:
    """
    Binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LinkedListNode:
    """
    Linked list node.
    """
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    """
    Linked list.
    """
    def __init__(self, val: int):
        """
        Initialize with value at head.
        """
        node = LinkedListNode(val)
        self.head = node
        self.tail = node
        self.length = 1
    
    def add(self, val: int):
        """
        Add new node.
        """
        node = LinkedListNode(val)
        self.head.next = node
        self.head = node
        self.length += 1
    
    def asInteger(self):
        """
        Represent linked list of integers as single integer.
        """
        node = self.tail
        vals = [None] * self.length
        i = 0
        while node is not None:
            vals[i] = node.val
            node = node.next
            i += 1
        vals = list(reversed(vals))
        return int("".join(map(str, vals))) 

def isLeaf(node: TreeNode):
    """
    Return True if node is leaf, else return False.
    """
    if node.left or node.right:
        return False
    return True

def rootToLeafNumbers(node: TreeNode) -> List[LinkedList]:
    """
    Get root-to-leaf numbers
    """
    if not node:
        return None
    if isLeaf(node):
        return [LinkedList(node.val)]
    numbers = []
    left = rootToLeafNumbers(node.left)
    if left is not None:
        for seq in left:
            seq.add(node.val)
            numbers += [seq]
    right = rootToLeafNumbers(node.right)
    if right is not None:
        for seq in right:
            seq.add(node.val)
            numbers += [seq]
    return numbers

def sumNumbers(root: TreeNode) -> int:
    """
    Get sum of all root-to-leaf numbers.
    """
    if not root:
        return 0
    numbers = rootToLeafNumbers(root)
    numbers = [digits.asInteger() for digits in numbers]
    return sum(numbers)

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return sumNumbers(root)                
