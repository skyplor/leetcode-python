from typing import List

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    '''
      treat the numbers in this array as indices
      access the first element and follow it's index to go to the next element
      
      Floyd's cycle detection algorithm
      using 2 pointers, we will be able to know when they collide.
      once they collide, move the slow pointer back to first element,
      now make both pointers move 1 step at a time.
      The next time they meet will be at the start of the cycle.
      This will be the duplicated number
    '''
    fast = slow = 0
    while True:
      slow = nums[slow]
      fast = nums[nums[fast]]
      if fast == slow:
        break
    
    slow = 0
    while True:
      slow = nums[slow]
      fast = nums[fast]
      if fast == slow:
        return fast
  
sol = Solution()
nums = [3, 3, 3, 3, 3]
output = sol.findDuplicate(nums)
print(f'nums: {nums}\noutput: {output}')