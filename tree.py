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
    queue = Queue()
    queue.put(root)
    level = 1
    start_index = int(math.pow(2, level-1))
    end_index = int(math.pow(2, level) + 1)
    values_level = values[start_index:end_index]


class TestTree(TestCase):
    def test1(self) -> None:
        values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root = get_tree_from_list(values=values)
