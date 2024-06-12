from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    l, r = 0, 1
    while r < len(prices):
      buy = prices[l]
      sell = prices[r]
      profit = 0
      if buy < sell:
        profit = sell - buy
      else:
        l = r
      r += 1

      max_profit = max(max_profit, profit)

    return max_profit
  
sol = Solution()
input = [3,2,6,5,0,3]
# input = [7,6,4,3,1]
# input = [7,1,5,3,6,4]
output = sol.maxProfit(input)
print(f'Input: {input}\nOutput: {output}')