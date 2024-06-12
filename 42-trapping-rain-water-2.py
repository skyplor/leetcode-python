from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    output = 0
    max_lefts = [0] * len(height)
    max_rights = [0] * len(height)

    for i in range(1, len(height)):
      if len(height[0:i]) > 0:
        max_lefts[i] = max(height[0:i])
    for i in range(0, len(height) - 1):
      if len(height[i + 1:]) > 0:
        max_rights[i] = max(height[i + 1:])

    for i in range(0, len(height)):
      output += max(0, min(max_lefts[i], max_rights[i]) - height[i])

    return output

sol = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
output = sol.trap(input)
print(f'Input: {input}\nOutput: {output}')