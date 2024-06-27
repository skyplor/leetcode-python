from typing import List

class Solution:
  def change(self, amount: int, coins: List[int]) -> int:
    '''
    using dfs, we can keep iterating and add the result into dp.
    '''
    dp = {}
    
    def dfs(i, a):
      if amount < a:
        return 0
      if amount == a:
        return 1
      if i == len(coins):
        return 0
      if (i, a) in dp:
        return dp[(i, a)]

      dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
      return dp[(i, a)]
      
    return dfs(0, 0)
  
sol = Solution()
amount = 5
coins = [1,2,5]
print(f'output: {sol.change(amount, coins)}')