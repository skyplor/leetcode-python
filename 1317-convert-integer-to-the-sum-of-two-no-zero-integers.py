class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        '''
        We just have a loop from 1 to n and each time we get the complementary number and also check if both numbers have non-zero digits. If yes then we return as result
        '''
        def all_non_zero_digits(i: int) -> bool:
            while i != 0:
                i, digit = divmod(i, 10)
                if digit == 0:
                    return False
                
            return True
        
        for first in range(1, n):
            second = n - first
            if all_non_zero_digits(first) and all_non_zero_digits(second):
                return [first, second]
            
        return []
        
sol = Solution()
n = 2
print(f'output: {sol.getNoZeroIntegers(n)}')
n = 11
print(f'output: {sol.getNoZeroIntegers(n)}')