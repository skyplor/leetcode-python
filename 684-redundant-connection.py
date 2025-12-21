from collections import deque, defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        We can use union-find data structure for this case. 
        For union find, we will go through the list of edges, and each time we get the parent of the first node, get the parent of the 2nd node, and if it's different, we connect the parent to the first node's parent
        after that we go to the next in the list, and if we try to add but the parents of both nodes are already connected, then we have found a cycle
        '''
        # initialise all nodes to be a parent of its own
        # Graph theory (no cycle, number of nodes = n, number of edges = n - 1)
        # because for this case, we have 1 additional edge (thus making this a cycle), that means the number of edges == number of nodes.
        # so we can just use length of edges
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        # find the parent
        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])

            return parent[n]

        # merge 2 nodes
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
                
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []

sol = Solution()
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
output = sol.findRedundantConnection(edges)
print(f'output: {output}')
