from graphnode import Node, buildGraph
from typing import Optional
from collections import deque

class Solution:
  def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
    clone_map = {}
    
    def dfs(node):
      if node in clone_map:
        return clone_map[node]
      else:
        new_node = Node(node.val)
        clone_map[node] = new_node
        for neighbor in node.neighbors:
          new_node.neighbors.append(dfs(neighbor))
          
      return new_node
        
    return dfs(node) if node else None
    
sol = Solution()
adjList = [[2,4],[1,3],[2,4],[1,3]]
node = buildGraph(adjList)
print(node)
cloned_node = sol.cloneGraph(node)
print(cloned_node)