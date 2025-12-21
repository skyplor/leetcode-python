from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        '''
        Treat this as a tree (graph without cycles).

        Key insight: Any subtree with a sum divisible by k can be split off 
        as a separate component. We count all such possible components by:
            1. Building adjacency list for the tree
            2. Using DFS to calculate subtree sums bottom-up
            3. Whenever a subtree sum is divisible by k, increment the count
            4. Track parent to avoid revisiting nodes in the tree traversal
        '''
        adj_list = defaultdict(list)
        for first, second in edges:
            adj_list[first].append(second)
            adj_list[second].append(first)

        res = 0
        def dfs(cur, parent):
            total = values[cur]

            for child in adj_list[cur]:
                if child != parent:
                    total += dfs(child, cur)

            if total % k == 0:
                nonlocal res
                res += 1

            return total

        dfs(0, -1)
        return res
        
        
sol = Solution()
print(f'output: {sol.maxKDivisibleComponents(n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6)}, expected: 2')
print(f'output: {sol.maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3)}, expected: 3')