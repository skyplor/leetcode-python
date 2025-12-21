class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        '''
        We get the prefix sum at each index

        Next, we have a loop that will have the integers that are divisible by k up to length of the nums, eg for d = k; d<len(nums); d+=k
        Then, we have another inner loop that will create the window from i = 0 to len(nums) - d nums[i..i+d]

             - at each iteration, we get the sum based on prefix_sum at i+d - prefix_sum at i - 1
             - Then we compare with the max sum and if it's higher, replace with this sum.

        At the end return the max sum
        
        Note: This solution is not efficient enough as it gave TLE
        '''
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        res = float('-inf')
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        for d in range(k, n+1, k):
            for i in range(0, n - d + 1):
                curr_sum = prefix_sum[i+d] - prefix_sum[i]
                res = max(res, curr_sum)

        return res

sol = Solution()
print(f'output: {sol.maxSubarraySum(nums = [1,2], k = 1)}, expected: 3')
print(f'output: {sol.maxSubarraySum(nums = [-1,-2,-3,-4,-5], k = 4)}, expected: -10')
print(f'output: {sol.maxSubarraySum(nums = [-5,1,2,-3,4], k = 2)}, expected: 4')