from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # strs = ["eat","tea","tan","ate","nat","bat"]
      # sorted = {'aet': ["eat", "tea"]}
      sorted_map = defaultdict(list)
      for word in strs:
        key = ''.join(sorted(word))
        sorted_map[key].append(word)

      return list(sorted_map.values())
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))