class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        '''
        A valid tree is an undirected graph with no cycles and it can only have 1 component
        We can go with union-find for this
        Also, a valid tree without cycle must have exactly n-1 edges
        '''
        if len(edges) != n - 1:
            return False

        parents = {i: i for i in range(n)}
        sizes = {i: 1 for i in range(n)}
        
        def find(node):
            res = node
            while parents[res] != res:
                parents[res] = parents[parents[res]]
                res = parents[res]
                
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if sizes[p1] > sizes[p2]:
                parents[p2] = p1
                sizes[p1] += sizes[p2]
            else:
                parents[p1] = p2
                sizes[p2] += sizes[p1]
                
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
            
        return True
    
sol = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
output = sol.validTree(n, edges)
print(f'output: {output}')