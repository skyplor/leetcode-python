class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        '''
        We just need to know the shortest distance between (x and z) vs (y and z)
        Distance will be absolute difference as the direction can be either way.
        '''
        diff = abs(x - z) - abs(y - z) 
        if diff == 0: return 0
        if diff < 0: return 1
        return 2
    
sol = Solution()
x = 2
y = 7
z = 4
print(f'output: {sol.findClosest(x, y, z)}, expected: 1')
x = 2
y = 5
z = 6
print(f'output: {sol.findClosest(x, y, z)}, expected: 2')
x = 1
y = 5
z = 3
print(f'output: {sol.findClosest(x, y, z)}, expected: 0')