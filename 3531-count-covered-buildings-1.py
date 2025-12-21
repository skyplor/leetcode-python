class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        '''
        We go through each building, for each column (x-value), we find the first and last point (y-value). These are the buildings that are not covered at the x-axis
            - To find the first and last point, we have a hash map of key: x-value and val: (first y-value, last y-value)
            - Each time we will compare the first y-value and if the current point is < first y-value, replace it. Similarly, for last y-value is if the point is > y-value
        Then we repeat again for each row (y-value)
        In the end we go through each building again and only take those buildings that have coordinates (min_x < x < max_x, min_y < y < max_y)
        '''
        x_grouping = {i: (float('inf'), float('-inf')) for i in range(1, n+1)}
        for x, y in buildings:
            min_y, max_y = x_grouping[x]
            x_grouping[x] = (min(min_y, y), max(max_y, y))

        y_grouping = {i: (float('inf'), float('-inf')) for i in range(1, n+1)}
        for x, y in buildings:
            min_x, max_x = y_grouping[y]
            y_grouping[y] = (min(min_x, x), max(max_x, x))

        covered = 0
        for x, y in buildings:
            min_y, max_y = x_grouping[x]
            min_x, max_x = y_grouping[y]
            if min_x < x < max_x and min_y < y < max_y:
                covered += 1
                
        return covered
            
        
sol = Solution()
print(f'output: {sol.countCoveredBuildings(n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]])}, expected: 1')
print(f'output: {sol.countCoveredBuildings(n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]])}, expected: 0')
print(f'output: {sol.countCoveredBuildings(n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]])}, expected: 1')
print(f'output: {sol.countCoveredBuildings(n = 3, buildings = [(1,1), (1,2), (1,3)])}, expected: 0')