from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    # l, r, m_area
    m_area = 0
    l = 0
    r = len(height) - 1
    while l < r:
      left = height[l]
      right = height[r]
      min_height = min(left, right)
      d = r - l
      c_area = min_height * d
      m_area = max(m_area, c_area)
      if left < right:
        l +=1
      else:
        r -=1
    return m_area
  
sol = Solution()
# height = [1, 1]
height = [1,8,6,2,5,4,8,3,7]
output = sol.maxArea(height)
print(f'Height: {height}\nOutput: {output}')