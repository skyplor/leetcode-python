from typing import List
from heapq import heappush, heappop

'''
We use quick select to allow for an average time complexity of o(n)
in the first implementation using heap, average time complexity is O(n + klogn)
'''
class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    index = len(nums) - k
    
    def quickSelect(l, r):
      pivot, p = nums[r], l
      for i in range(l, r):
        if nums[i] <= pivot:
          nums[p], nums[i] = nums[i], nums[p]
          p += 1
          
      nums[p], nums[r] = pivot, nums[p]
      
      if p > index:
        return quickSelect(l, p - 1)
      elif p < index:
        return quickSelect(p + 1, r)
      else:
        return nums[p]
    
    return quickSelect(0, len(nums) - 1)
sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
output = sol.findKthLargest(nums, k)
print(f'nums: {nums}\nk: {k}\noutput: {output}')