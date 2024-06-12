from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    output = 0
    l = 0
    r = len(height) - 1
    l_max = height[l]
    r_max = height[r]
    while l < r:
      if l_max < r_max:
        l += 1
        l_max = max(height[l], l_max)
        output += max(0, l_max - height[l])
      else:
        r -= 1
        r_max = max(height[r], r_max)
        output += max(0, r_max - height[r])

    return output

sol = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
output = sol.trap(input)
print(f'Input: {input}\nOutput: {output}')