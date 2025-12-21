from graphnode import Node, buildGraph
from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        clones = {}
        queue = deque()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            if cur not in clones:
                clone = Node(cur.val, cur.neighbors)
                clones[cur] = clone
            for n in cur.neighbors:
                if n not in clones:
                    queue.append(n)

        for clone in clones.values():
            new_neighbors = []
            for neighbor in clone.neighbors:
                cloned_neighbor = clones[neighbor]
                new_neighbors.append(cloned_neighbor)

            clone.neighbors = new_neighbors

        return clones[node]


sol = Solution()
adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
node = buildGraph(adjList)
print(node)
cloned_node = sol.cloneGraph(node)
print(cloned_node)
