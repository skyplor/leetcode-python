from collections import defaultdict
from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    num_occurrence = defaultdict(list)
    processed_nums = []
    for n in nums:
      if n in processed_nums:
        continue
      count = nums.count(n)
      num_occurrence[count].append(n)
      processed_nums.append(n)

    result = []
    for i in reversed(range(1, len(nums) + 1)):
      if len(num_occurrence[i]) > 0:
        result.extend(num_occurrence[i])
        if len(result) >= k:
          break

    return result
sol = Solution()
print(sol.topKFrequent([-1, -1], 1))