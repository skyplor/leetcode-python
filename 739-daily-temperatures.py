from typing import List

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # using a stack, we push in the index of each temperature if the next value is lesser
    # if next value on stack is smaller than current value, 
    # we pop from the stack and get the difference between the indices of the current value and the elements in the stack
    stack = []
    res = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
      while stack and t > temperatures[stack[-1]]:
        index = stack.pop()
        res[index] = i - index
      stack.append(i)

    return res
  
sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
output = sol.dailyTemperatures(temperatures)
print(f'temperatures: {temperatures}\noutput: {output}')