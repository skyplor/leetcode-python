from typing import List
from math import ceil

class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    stack = []
    pair = [[p, s] for p, s in zip(position, speed)]
    
    for p, s in sorted(pair)[::-1]:
      stack.append((target - p) / s)
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()
    return len(stack)
  
sol = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
output = sol.carFleet(target, position, speed)
print(f'target: {target}\nposition: {position}\nspeed: {speed}\noutput: {output}')