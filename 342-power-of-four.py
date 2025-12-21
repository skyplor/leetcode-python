from numbers import Number
from math import log

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''
        n = 4^x
        log₂(n) = x log₂(4)
        log₂(n) = 2x
        x = log₂(n) / 2
        '''
        if n <= 0:
            return False

        x = log(n, 2)
        return x % 2 == 0
    
sol = Solution()
n = 16
print(f'output: {sol.isPowerOfFour(n)}, expected: True')
n = 5
print(f'output: {sol.isPowerOfFour(n)}, expected: False')
n = 1
print(f'output: {sol.isPowerOfFour(n)}, expected: True')
n = -128
print(f'output: {sol.isPowerOfFour(n)}, expected: False')
n = 2
print(f'output: {sol.isPowerOfFour(n)}, expected: False')
n = 64
print(f'output: {sol.isPowerOfFour(n)}, expected: True')