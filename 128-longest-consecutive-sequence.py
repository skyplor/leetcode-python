from typing import List

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    nums_set = set(nums)
    longest_consecutive = 0
    for num in nums:
      if (num - 1 not in nums_set):
        current_consecutive = 1
        current_key = num + 1
        while current_key in nums_set:
          current_consecutive += 1
          current_key += 1

      longest_consecutive = max(current_consecutive, longest_consecutive)
        
    return longest_consecutive
  
sol = Solution()
input = [101, 100, 102, 1, 3, 4, 2, 200]
print(f'Input: {input}\nOutput: {sol.longestConsecutive(input)}')