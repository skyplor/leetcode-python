class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        '''
        We go through each building, we store the min_y, max_y, min_x, max_x for each row and column respectively
        In the end we go through each building again and only take those buildings that have coordinates (min_x < x < max_x, min_y < y < max_y)
        '''
        min_y = [float('inf')] * (n+1)
        min_x = [float('inf')] * (n+1)
        max_y = [float('-inf')] * (n+1)
        max_x = [float('-inf')] * (n+1)
        for x, y in buildings:
            min_y[x] = min(y, min_y[x])
            min_x[y] = min(x, min_x[y])
            max_y[x] = max(y, max_y[x])
            max_x[y] = max(x, max_x[y])

        res = 0
        for x, y in buildings:
            if min_x[y] < x < max_x[y] and  min_y[x] < y < max_y[x]:
                res += 1
                
        return res

        
sol = Solution()
print(f'output: {sol.countCoveredBuildings(n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]])}, expected: 1')
print(f'output: {sol.countCoveredBuildings(n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]])}, expected: 0')
print(f'output: {sol.countCoveredBuildings(n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]])}, expected: 1')
print(f'output: {sol.countCoveredBuildings(n = 3, buildings = [(1,1), (1,2), (1,3)])}, expected: 0')