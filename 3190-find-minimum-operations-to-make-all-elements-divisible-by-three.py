class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        '''
        Go through each num, if num % 3 != 0, add 1 to the result
        '''
        res = 0
        for num in nums:
            if num % 3 != 0:
                res += 1

        return res


sol = Solution()
print(f'output: {sol.minimumOperations([1, 2, 3, 4])}, expected: 3')
print(f'output: {sol.minimumOperations([3, 6, 9])}, expected: 0')
