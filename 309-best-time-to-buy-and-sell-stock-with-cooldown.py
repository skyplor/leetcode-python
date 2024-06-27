from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    '''
              sell
             1, 2, 3, 4, 5
         1 [+0,+1,+2,-1,+1] 
         2 [+0,+0,+1,-2,+0]
    buy  3 [+0,+0,+0,-3,-2]
         4 [+0,+0,+0,+0,+2]
         5 [+0,+0,+0,+0,+0]
         
    using a decision tree, each time it's either buy/sell + cooldown
                                    0
                            /               \\
    Day 0                  B                 CD
                           -1                 0
                    /            \\         /   \\
    Day 1         S                CD      B     CD
                  +1               -1
                  |               /   \\
    Day 2         CD             S    CD
                  +1            +2    -1
                /  \\            |   /   \\
    Day 3       B   CD          CD   S    CD
              +1     +1         +2   -1   -1
              /\\    |\\        / \\   |    / \\
    Day 4    S   CD  B CD      B   CD  CD   S  CD
            +3   +1  -1 +1    +0   +2  -1  +1  -1
            
    State: Buy or Sell
    If Buy -> i + 1
    If Sell -> i + 2 (because must Cooldown)
    '''
    dp = {}
    
    def dfs(i, buying):
      if i >= len(prices):
        return 0
      if (i, buying) in dp:
        return dp[(i, buying)]
      if buying:
        buy = dfs(i+1, not buying) - prices[i]
        cooldown = dfs(i+1, buying)
        dp[(i, buying)] = max(buy, cooldown)
      else:
        sell = dfs(i+2, not buying) + prices[i]
        cooldown = dfs(i+1, buying)
        dp[(i, buying)] = max(sell, cooldown)
        
      return dp[(i, buying)]
    
    return dfs(0, True)

sol = Solution()
prices = [1,2,3,0,2]
output = sol.maxProfit(prices)
print(f'output: {output}')