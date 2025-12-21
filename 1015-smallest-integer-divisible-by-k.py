class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        '''
        if k is even or multiple of 5, return -1 since the value will never be an even number or multiple of 5
        Each iteration we will multiply cur by 10 + 1 and % k to get the remainder to test against

        Then we get the mod. Using pigeonhole theory, if there are no result after k times, then we are certain that it will not have a result
        
        Note: if we don't % k and use `cur` instead, it can be a big number and calculation would take longer.
        By taking the mod and working on the mod, we can work on a smaller number
        '''
        if k % 2 == 0 or k % 5 == 0:
            return -1

        i = 1
        rem = 1
        while rem % k != 0 and i <= k:
            rem = ((rem * 10) + 1) % k
            i += 1

        return i


sol = Solution()
print(f'output: {sol.smallestRepunitDivByK(1)}, expected: 1')
print(f'output: {sol.smallestRepunitDivByK(2)}, expected: -1')
print(f'output: {sol.smallestRepunitDivByK(3)}, expected: 3')
