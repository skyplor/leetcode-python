class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        '''
        since we want contiguous subarrays, that means we will loop through each group, each group will be of `k` length. We can probably use DP for this and have a function to recursively solve for `l` and `r` to return the sum of the elements
        Base case is if the l:r passed in is <= k:
            - Then we return k * max(arr[l:r])
        '''
        n = len(arr)
        dp = [-1] * (n+1)

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            cur_max = 0
            res = 0
            for j in range(i, min(i + k, n)):
                cur_max = max(cur_max, arr[j])
                window_size = j - i + 1
                res = max(res, dfs(j+1) + (window_size * cur_max))
            dp[i] = res
            return res

        return dfs(0)


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
