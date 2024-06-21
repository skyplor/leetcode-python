from typing import List

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    '''
    At each step, we determine the minimum cost to reach that step.
    If there are multiple ways to reach that step, we get the way with the minimum cost
    base cases:
      to reach index 0: minCost = cost[0]
      to reach index 1: minCost = cost[1]
      to reach index 2: minCost = min((minCost(1) + cost[2]), (minCost(0) + cost[2]))
      to reach index 3: minCost = min((minCost(2) + cost[3]), (minCost(1) + cost[3]))
    '''
    for i in range(len(cost) - 3, -1, -1):
      # cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
      # simplies to
      # cost[i] = cost[i] + min(cost[i+1], cost[i+2])
      cost[i] += min(cost[i+1], cost[i+2])

    return min(cost[0], cost[1])

sol = Solution()
cost = [10,15,20]
output = sol.minCostClimbingStairs(cost)

print(f'cost: {cost}\noutput: {output}')