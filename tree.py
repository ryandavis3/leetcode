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


def get_max_level(values: List[int]) -> int:
    L = len(values)
    total = 1
    level = 1
    while total < L:
        total += int(math.pow(2, level))
        level += 1
    return level


def get_tree_from_list(values: List[int]) -> TreeNode:
    # Root node of tree
    root = TreeNode(x=values[0])
    # Queue for previous llevel
    prev = Queue()
    prev.put(root)
    level = 1
    # Initialize dictionary with visit count for each node
    visits: Dict[int, int] = {}
    for value in values:
        visits[value] = 0
    # Get max level of tree
    max_level = get_max_level(values=values)
    # Iterate by level
    while level < max_level:
        # Get start and end indices for level
        start_index = int(math.pow(2, level)) - 1
        end_index = int(math.pow(2, level + 1)) - 1
        # Build queue for current levels
        x_level = values[start_index:end_index]
        curr = Queue()
        for x in x_level:
            if x is None:
                node = None
            else:
                node = TreeNode(x=x)
            curr.put(node)
        # Connect current level with previous level
        parent = prev.get()
        next = Queue()
        while not curr.empty():
            if visits[parent.val] == 2 or parent is None:
                parent = prev.get()
            node = curr.get()
            next.put(node)
            if visits[parent.val] == 0:
                parent.left = node
                visits[parent.val] += 1
            elif visits[parent.val] == 1:
                parent.right = node
                visits[parent.val] += 1
        # Increment to next level
        prev = next
        level += 1
    return root


class TestTree(TestCase):
    def test1(self) -> None:
        values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root = get_tree_from_list(values=values)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 5)
        self.assertEqual(root.right.val, 1)
        self.assertEqual(root.left.right.val, 2)
        self.assertEqual(root.left.right.left.val, 7)
        self.assertEqual(root.left.right.right.val, 4)

    def test2(self) -> None:
        values = [1, 2, 3]
        root = get_tree_from_list(values=values)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)

    def test3(self) -> None:
        values = [1, 2, None, 3, 4]
        root = get_tree_from_list(values=values)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.left.left.val, 3)
        self.assertEqual(root.left.right.val, 4)

    def test_get_max_level1(self) -> None:
        values = [1, 2, 3]
        max_level = get_max_level(values=values)
        self.assertEqual(max_level, 2)

    def test_get_max_level2(self) -> None:
        values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        max_level = get_max_level(values=values)
        self.assertEqual(max_level, 4)