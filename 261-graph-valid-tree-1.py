from collections import deque, defaultdict


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        '''
        A valid tree is an undirected graph with no cycles and it can only have 1 component
        We can use BFS for this
        Also, at the end we need to check if we have visited ALL nodes
        we also need an adj list to store all neighbours of a node. We need to store both ways as this is undirected graph
        '''
        if len(edges) != n-1:
            return False

        visited = set()
        queue = deque()
        neighbours = defaultdict(list)
        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)

        queue.append(0)
        visited.add(0)
        while queue:
            current = queue.popleft()
            for neighbour in neighbours[current]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

        return len(visited) == n


sol = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
output = sol.validTree(n, edges)
print(f'output: {output}')
