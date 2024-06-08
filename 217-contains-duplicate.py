from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        result = True
        for value in nums:
          if value in dict:
            return False
          dict[value] = True

        return result
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4, 2]))