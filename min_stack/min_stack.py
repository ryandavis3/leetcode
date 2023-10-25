import unittest
import uuid
from typing import Optional


class Node:
    def __init__(self, value: int, prev, node_id: str):
        self.value = value
        self.prev = prev
        self.node_id = node_id


class MinStack:

    def __init__(self):
        self._head = None
        self._min = None

    def push(self, val: int) -> None:
        node_id = str(uuid.uuid4())
        node = Node(value=val, prev=self._head, node_id=node_id)
        self._head = node
        if self._min is None:
            self._min = Node(value=val, prev=None, node_id=node_id)
        elif val < self._min.value:
            self._min = Node(value=val, prev=self._min, node_id=node_id)

    def pop(self) -> None:
        if self._head is None:
            raise ValueError('No head available!')
        self._head = self._head.prev

    def top(self) -> int:
        if self._head is None:
            raise ValueError('No head available!')
        top_value = self._head.value
        return top_value

    def getMin(self) -> int:
        # Get the minimum element in the stack
        pass

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class TestMinStack(unittest.TestCase):

    def test_top(self) -> None:
        stack = MinStack()
        stack.push(val=1)
        stack.push(val=2)
        top = stack.top()
        self.assertEqual(top, 2)
        stack.pop()
        top = stack.top()
        self.assertEqual(top, 1)

