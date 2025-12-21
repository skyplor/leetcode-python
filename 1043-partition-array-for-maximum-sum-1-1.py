class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        '''
        since we want contiguous subarrays, that means we will loop through each group, each group will be of `k` length. We can probably use DP for this and have a function to recursively solve for `l` and `r` to return the sum of the elements
        Base case is if the l:r passed in is <= k:
            - Then we return k * max(arr[l:r])
        '''

        def solve(l: int, r: int) -> int:
            if r - l + 1 <= k:
                num_elements = r - l + 1
                return num_elements * max(arr[l:r+1])

            max_sum = 0

            for i in range(1, k+1):
                max_sum = max(max_sum, solve(l, l + i - 1) + solve(l + i, r))

            return max_sum

        return solve(0, len(arr) - 1)


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
