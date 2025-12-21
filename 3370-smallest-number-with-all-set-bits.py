class Solution:
    def smallestNumber(self, n: int) -> int:
        '''
        We generate from 1 then each time we shift the bits by 1 to the left and add 1 to it
        '''
        res = 1
        while res < n:
            res = (res << 1) + 1

        return res


sol = Solution()
print(f'output: {sol.smallestNumber(5)}, expected: 7')
print(f'output: {sol.smallestNumber(10)}, expected: 15')
print(f'output: {sol.smallestNumber(3)}, expected: 3')
