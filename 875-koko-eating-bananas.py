from typing import List
from math import ceil

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # max speed is to eat 1 pile per hour
    # to allow eating of 1 pile per hour, the min K will be equal to the number of bananas of the highest pile
    # that is the upper bound. 1 will be the lower bound
    # we then use binary search to find the min K
    upperK = max(piles)
    lowerK = 1
    res = upperK

    while lowerK <= upperK:
      k = lowerK + (upperK - lowerK) // 2
      hours = 0
      for pile in piles:
          hours += ceil(float(pile) / k)
      if hours <= h:
        res = k
        upperK = k - 1
      else:
        lowerK = k + 1
    return res

sol = Solution()
# piles = [3,6,7,11]
# h = 8
# piles = [30,11,23,4,20]
# h = 5
# piles = [30,11,23,4,20]
# h = 6
piles = [4]
h = 3
output = sol.minEatingSpeed(piles, h)
print(f'piles: {piles}\nh: {h}\noutput: {output}')