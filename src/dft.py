"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T
from collections import deque


def in_order(t: T) -> Iterable[int]:
    # Create empty an stack
    stack = deque()

    # set the current node to the root node
    node = t

    # if the current node is None and the stack is also empty, we are done
    while stack or node:
        # if current node exists, push it into stack and move to its left child
        if node:
            stack.append(node)
            node = node.left
        else:
            # Otherwise, if the current node is None, pop an element from the child
            node = stack.pop()
            yield node.val
            node = node.right




