class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        '''
        using a loop, we will shift the LSB and if it was a 1, we add to the ops. If it was 0, then we don't
        '''
        res = 0
        while n:
            res ^= n
            n >>= 1
        return res


sol = Solution()
print(f'output: {sol.minimumOneBitOperations(3)}, expected: 2')
print(f'output: {sol.minimumOneBitOperations(6)}, expected: 4')
