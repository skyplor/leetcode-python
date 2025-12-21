class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        '''
        We get the prefix sum at each index

        For each index i (0-indexed in nums):
            - offset = (i+1) % k
            - Valid subarrays ending at i have starting positions j where (j+1) % k == offset
            - Max subarray sum ending at i = prefix_sum[i+1] - min_prefix[offset]
            - Update res with this maximum
            - Update min_prefix[offset] = min(min_prefix[offset], prefix_sum[i+1])

        Return res
        '''
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0
        total = 0

        res = float('-inf')
        for i, num in enumerate(nums):
            total += num
            offset = (i+1) % k
            res = max(res, total - min_prefix[offset])
            min_prefix[offset] = min(min_prefix[offset], total)

        return res


sol = Solution()
print(f'output: {sol.maxSubarraySum(nums=[1, 2], k=1)}, expected: 3')
print(
    f'output: {sol.maxSubarraySum(nums=[-1, -2, -3, -4, -5], k=4)}, expected: -10')
print(
    f'output: {sol.maxSubarraySum(nums=[-5, 1, 2, -3, 4], k=2)}, expected: 4')
