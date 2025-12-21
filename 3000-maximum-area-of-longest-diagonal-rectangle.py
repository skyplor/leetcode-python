from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        '''
        diagonal length = sqrt(length^2 + width^2)
        Since we are comparing all dimensions to get the one with the longest, that means we don't really need to do sqrt as well. So we can just use (length**2 + width**2). We store both the max_diagonal and the max_area.
        If encounter same max_diagonal, then we update max_area
        
        Time: O(n)
        Space: O(1)
        '''
        max_diagonal = max_area = float('-inf')
        for length, width in dimensions:
            cur_diagonal = length**2 + width**2
            if cur_diagonal > max_diagonal:
                max_diagonal = cur_diagonal
                max_area = length*width
            elif cur_diagonal == max_diagonal:
                max_diagonal = cur_diagonal
                max_area = max(max_area, length*width)
        
        return max_area
    
sol = Solution()
dimensions = [[9,3],[8,6]]
print(f'output: {sol.areaOfMaxDiagonal(dimensions)}')

dimensions = [[3,4],[4,3]]
print(f'output: {sol.areaOfMaxDiagonal(dimensions)}')

dimensions = [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]
print(f'output: {sol.areaOfMaxDiagonal(dimensions)}')