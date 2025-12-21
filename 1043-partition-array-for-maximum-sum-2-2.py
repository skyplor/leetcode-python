class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        '''
        since we want contiguous subarrays, that means we will loop through each group, each group will be of `k` length. We can use DP for this
        We create a 1-D DP. At each index, we store the maximum sum that is possible based on k different scenarios.

        We compute bottom-up:
            if k = 3
            - index 0, max_sum = arr[0]
            - index 1, max_sum = max(arr[1] + dp[0])
            - index 2, max_sum = max(arr[2] + dp[1], max(arr[1:2]) + dp[0])
            - index 3, max_sum = max(arr[3] + dp[2], max(arr[2:3]) + dp[1], max(arr[1:3]) + dp[0])
            - ...
            - index i, max_sum = max(arr[n] + dp[i - 1], max(arr[i-1:i+1]))
        '''
        dp = [0] * k
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            cur_max = 0
            max_at_i = 0

            for j in range(i, max(-1, i - k), -1):
                cur_max = max(cur_max, arr[j])
                window_size = i - j + 1
                cur_sum = cur_max * window_size
                sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
                max_at_i = max(max_at_i, cur_sum + sub_sum)

            dp[i % k] = max_at_i
            
        return dp[(len(arr) - 1) % k]

sol = Solution()
arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
print(f'output: {sol.maxSumAfterPartitioning(arr, k)}, expected: 84')
arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
k = 4
print(f'output: {sol.maxSumAfterPartitioning(arr, k)}, expected: 83')
arr = [1]
k = 1
print(f'output: {sol.maxSumAfterPartitioning(arr, k)}, expected: 1')
