class Solution:
    def countCollisions(self, directions: str) -> int:
        '''
        Those "L" on the left, "R" on the right and "S" in the middle are irrelevant
        '''
        directions = directions.lstrip('L').rstrip('R').replace('S', '')
        return len(directions)


sol = Solution()
print(f'output: {sol.countCollisions("RLRSLL")}, expected: 5')
print(f'output: {sol.countCollisions("LLRR")}, expected: 0')
print(f'output: {sol.countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR")}, expected: 20')
