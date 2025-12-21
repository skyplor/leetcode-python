from typing import List


class Solution:
    '''
    e.g [
            [1, 1, 0]
            [1, 1, 0]
            [0, 0, 1]
        ]

    '''

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        Using union by rank
        '''
        n = len(isConnected)
        parents = [i for i in range(n)]
        ranks = [0] * n

        def find(node: int):
            res = node
            while res != parents[res]:
                # we do compression bit-by-bit so over time, if there are a lot of traversals, the tree will be flattened
                parents[res] = parents[parents[res]]
                res = parents[res]

            return res

        def union(fromNode: int, toNode: int) -> bool:
            fromParent = find(fromNode)
            toParent = find(toNode)

            if fromParent == toParent:
                return False

            if ranks[toParent] > ranks[fromParent]:
                parents[fromParent] = toParent
            elif ranks[fromParent] > ranks[toParent]:
                parents[toParent] = fromParent
            else:
                parents[toParent] = fromParent
                ranks[fromParent] += 1

            return True

        res = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and union(i, j):
                    res -= 1

        return res


sol = Solution()
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
output = sol.findCircleNum(isConnected)
print(f'output: {output}')
