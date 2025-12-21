class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        '''
        This is the same as Qn 3025
        '''
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        res = 0
        
        for i, (_, y1) in enumerate(points):
            bottom = float('-inf')
            for j in range(i+1, n):
                _, y2 = points[j]
                if bottom < y2 <= y1:
                    res += 1
                    bottom = y2
                    if bottom == y1:
                        break
                    
        return res
    
sol = Solution()
points = [[1,1],[2,2],[3,3]]
print(f'output: {sol.numberOfPairs(points)}, expected: 0')
points = [[6,2],[4,4],[2,6]]
print(f'output: {sol.numberOfPairs(points)}, expected: 2')
points = [[3,1],[1,3],[1,1]]
print(f'output: {sol.numberOfPairs(points)}, expected: 2')