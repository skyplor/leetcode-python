from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        Using union-find, we can combine components and find how many aren't connected
        '''
        parents = [i for i in range(n)]
        sizes = [1] * n
        res = n

        def find(n1: int) -> int:
            res = n1
            while parents[res] != res:
                parents[res] = parents[parents[res]]
                res = parents[res]

            return res

        def union(n1: int, n2: int) -> int:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if sizes[p1] > sizes[p2]:
                parents[p2] = p1
                sizes[p1] += sizes[p2]
            else:
                parents[p1] = p2
                sizes[p2] += sizes[p1]

            return 1

        for n1, n2 in edges:
            res -= union(n1, n2)
            
        return res


sol = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
output = sol.countComponents(n, edges)
print(f'n: {n}\nedges: {edges}\noutput: {output}')
