class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        '''
        We first sort the nums to ensure we are processing from smallest to largest number.
        Next, we maintain a `prev` that is the smallest value we have used so far.
        Based on this `prev`, we want to check if there's a value that we can assign within [-k, k] to be added to this num by comparing it against `prev` + 1
        '''
        nums.sort()
        res, prev = 0, -10**9
        for x in nums:
            if max(x - k, prev + 1) <= x + k:
                prev = max(x - k, prev + 1)
                res += 1
        return res


sol = Solution()
print(f'output: {sol.maxDistinctElements([1, 2, 2, 3, 3, 4], 2)}, expected: 6')
print(f'output: {sol.maxDistinctElements([4, 4, 4, 4], 1)}, expected: 3')
