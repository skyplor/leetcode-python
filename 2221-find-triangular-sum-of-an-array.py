class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        '''
        We can create a dp array of length n and initialise to nums
        Next we have a loop that goes from 0 to n-1, and each iteration we tabulate the column values.
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n-1, 0, -1):
            for j in range(i):
                nums[j] = (nums[j] + nums[j+1]) % 10

        return nums[0]


sol = Solution()
print(f'output: {sol.triangularSum([1, 2, 3, 4, 5])}, expected: 8')
print(f'output: {sol.triangularSum([5])}, expected: 5')
# print(f'output: {sol.triangularSum([2,6,6,5,5,3,3,8,6,4,3,3,5,1,0,1,3,6,9])}, expected: 0')
