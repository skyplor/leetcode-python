from typing import List
from collections import defaultdict

class Solution:
  # Solution 1:
  # def findRepeatedDnaSequences(self, s: str) -> List[str]:
  #   res = set()
  #   temp = set()
  #   start, end = 0, 10
  #   while end <= len(s):
  #     sequence = s[start:end]
  #     if sequence in temp:
  #       res.add(sequence)
  #     else:
  #       temp.add(sequence)
  #     end += 1
  #     start += 1
      
  #   return list(res)

  # Solution 2:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    res = defaultdict(int)
    start, end = 0, 10
    while end <= len(s):
      sequence = s[start:end]
      res[sequence] += 1
      end += 1
      start += 1
      
    return [k for k, v in res.items() if v > 1]

sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(f'output: {sol.findRepeatedDnaSequences(s)}')