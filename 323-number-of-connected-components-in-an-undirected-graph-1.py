from typing import List

class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    '''
    we need a parent array to store the parent of each node.
    We will loop through the node and using the edges, set each node to a common parent
    This way, we will have a smaller tree.
    We will also need to know the rank of each node, i.e the number of connected components to that node
    this is an optimization way where we link a node that has lesser components to a node that has more components
    Whenever we do a linking, we will decrement the number of nodes 'n' so at the end, we will know the number of connected components
    '''
    parent = [i for i in range(n)] # we start off with each node being a parent of its own
    rank = [1] * n
    
    def findParent(node):
      res = node
      while res != parent[node]:
        parent[node] = parent[parent[node]]
        res = parent[node]
      return res
    
    def union(n1, n2):
      p1, p2 = findParent(n1), findParent(n2)
      
      if p1 == p2:
        return 0
      
      if rank[n1] < rank[n2]:
        parent[n1] = parent[n2]
        rank[n2] += rank[n1]
      else:
        parent[n2] = parent[n1]
        rank[n1] += rank[n2]

      return 1
      
    res = n
    for n1, n2 in edges:
      res -= union(n1, n2)
    
    return res
    
sol = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
output = sol.countComponents(n, edges)
print(f'n: {n}\nedges: {edges}\noutput: {output}')