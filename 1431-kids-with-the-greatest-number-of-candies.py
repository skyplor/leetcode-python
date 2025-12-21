from typing import List

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    '''
    We will need to loop through the list of candies to know what is the current max
    '''
    maxCandy = 0
    for candy in candies:
      if candy > maxCandy:
        maxCandy = candy
        
    result = [False]*len(candies)
    for idx, candy in enumerate(candies):
      if candy+extraCandies >= maxCandy:
        result[idx] = True
        
    return result
  
sol = Solution()
candies = [12,1,12]
extraCandies = 10
output = sol.kidsWithCandies(candies, extraCandies)
print(f'output: {output}')