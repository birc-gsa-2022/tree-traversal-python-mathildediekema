"""A module for breadth-first traversal of trees."""

from collections import deque
import collections
import queue
from typing import Iterable
from tree import T

# The queue data structure can help up traverse one level at a time.
# The class deque is specially designed to provide fast and memory-
# efficient ways to append and pop items from both ends of the data-
# structure. Python's deques is useful for implementing queues and 
# stacks.

def bf_order(t: T | None) -> Iterable[int]:

    # Create queue with root node
    queue = deque([tree])
    
    # if the queue is None we are done
    while queue:
        # We pop the queue from the left
        node = queue.popleft()
        yield node.val
        # if current node has children to the left, push it into the queue
        if node.left:
            queue.append(node.left)
        # if current node has children to the right, push it into the queue
        if node.right:
            queue.append(node.right)
  





