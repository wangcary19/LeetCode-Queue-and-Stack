# March 4th, 2024
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

visited = {}

def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
        return node
    elif node in self.visited:
        return self.visited[node]
    else:
        copy = Node(node.val, [])
        self.visited[node] = copy
        if node.neighbors:
            copy.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return copy