from typing import List

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    # using a 1-d dp
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
      for c in coins:
        if (a - c) >= 0:
          dp[a] = min(dp[a], 1 + dp[a - c])
          
    return dp[amount] if dp[amount] != (amount + 1) else -1
    
  
sol = Solution()
coins = [1,2,5]
amount = 11
output = sol.coinChange(coins, amount)
print(f'coins: {coins}\namount: {amount}\noutput: {output}')