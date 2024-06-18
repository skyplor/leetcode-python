from typing import List

class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []
    
  def __repr__(self) -> str:
    return 'GraphNode\n - val: {}\n - neighbors: {})'.format(self.val, self.neighbors)
    
def buildGraph(nodesList: List[List[int]]) -> 'Node':
  nodes = {}
  for i in range(1, len(nodesList) + 1):
    if i not in nodes:
      node = Node(i)
      nodes[i] = node
      
  for i, neighborsList in enumerate(nodesList):
    node = nodes[i + 1]
    neighbors = []
    for neighborVal in neighborsList:
      neighborNode = nodes[neighborVal]
      neighbors.append(neighborNode)

    node.neighbors = neighbors

  return nodes[1]
