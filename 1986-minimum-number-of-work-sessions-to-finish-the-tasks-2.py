class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        '''
        For this type of questions, we can use bitmask DP
        '''

        n = len(tasks)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        valid_subsets = []

        for mask in range(1 << n):
            total_time = sum(tasks[i] for i in range(n) if mask & (1 << i))
            if total_time <= sessionTime:
                valid_subsets.append(mask)

        for mask in range(1 << n):
            if dp[mask] == float('inf'):
                continue
            for subset in valid_subsets:
                if mask & subset == 0:
                    dp[mask | subset] = min(dp[mask | subset], dp[mask] + 1)

        return dp[(1 << n) - 1]


sol = Solution()
print(f'output: {sol.minSessions([1, 2, 3], 3)} expected: 2')
# print(f'output: {sol.minSessions([3, 1, 3, 1, 1], 8)} expected: 2')
# print(f'output: {sol.minSessions([1, 2, 3, 4, 5], 15)} expected: 1')
