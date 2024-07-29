from typing import List

class Solution:
  def jump(self, nums: List[int]) -> int:
    '''
    Using something similar to BFS + Greedy
    left and right pointers will determine our window of the array
    To update pointers, our left pointer = r + 1, right pointer will be the furthest position we can jump to, so right pointer = max(l, r)
    '''
    res = 0
    l = r = 0
    while r < len(nums) - 1:
      farthest = 0
      for i in range(l, r+1):
        farthest = max(farthest, i + nums[i])
      l = r + 1
      r = farthest
      res += 1

    return res

sol = Solution()
nums = [2,3,1,1,4]
print(f'output: {sol.jump(nums)}')