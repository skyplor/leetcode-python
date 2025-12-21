from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        e.g
            Given: [1, 2, 5]
            {1: 1, 2: 1, 5: 1}
            We build up the dp from scratch up to the amount then return the amount
        '''
        dp = {c: 1 for c in coins}
        dp[0] = 0

        for i in range(amount + 1):
            if i in dp:
                continue

            potential_mins = [float('inf')]
            for c in coins:
                remaining_val = i - c
                if remaining_val > 0 and dp[remaining_val]:
                    potential_mins.append(dp[remaining_val])
            dp[i] = min(potential_mins) + 1

        return dp[amount] if dp[amount] != float('inf') else -1


sol = Solution()
coins = [1, 2, 5]
amount = 11
output = sol.coinChange(coins, amount)
print(f'coins: {coins}\namount: {amount}\noutput: {output}')
