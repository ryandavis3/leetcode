# Tree utilities.

import math
from queue import Queue
from typing import List
from unittest import TestCase


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_tree_from_list(values: List[int]) -> TreeNode:
    root = TreeNode(x=values[0])
    prev = Queue()
    prev.put(root)
    level = 1
    start_index = int(math.pow(2, level-1))
    end_index = int(math.pow(2, level) + 1)
    x_level = values[start_index:end_index]
    curr = Queue()
    for x in x_level:
        if x is None:
            node = None
        else:
            node = TreeNode(x=x)
        curr.put(node)
    parent = prev.get()
    while not curr.empty():
        node = curr.get()
        if parent.left is None:
            parent.left = node
        elif parent.right is None:
            parent.right = node
        else:
            parent = prev.get()
    prev = curr
    return root





class TestTree(TestCase):
    def test1(self) -> None:
        values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root = get_tree_from_list(values=values)

    def test2(self) -> None:
        values = [1, 2, 3]
        root = get_tree_from_list(values=values)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)